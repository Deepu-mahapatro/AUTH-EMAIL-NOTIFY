import os
import secrets
import logging 
import requests
from urllib.parse import urlencode

from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests as google_requests

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from users.models import User

#Google OAuth configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

GOOGLE_REDIRECT_URI = os.getenv(
    "GOOGLE_REDIRECT_URI",
    "http://127.0.0.1:8000/auth/google/callback/"
)

GOOGLE_AUTH_ENDPOINT = (
    "https://accounts.google.com/o/oauth2/v2/auth"
)

GOOGLE_SCOPES = "openid email profile"

GOOGLE_TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "index.html")


def health(request):
    """Confirms that the Django backend is running."""
    return JsonResponse({
        "status": "success",
        "message": "Django backend is running"
    })


def authentication_status(request):
    """
    Placeholder for now.
    Real Google authentication will be implemented later.
    """
    return JsonResponse({
        "authenticated": False,
        "message": "Google authentication is not connected yet"
    })

def google_login(request):
    try:
        state = secrets.token_urlsafe(32)
        logger.info("STEP 1: state generated")

        request.session["oauth_state"] = state
        logger.info("STEP 2: session saved")

        params = {
            "client_id": GOOGLE_CLIENT_ID,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "response_type": "code",
            "scope": GOOGLE_SCOPES,
            "state": state,
            "prompt": "select_account",
        }

        logger.info("STEP 3: OAuth parameters created")

        auth_url = f"{GOOGLE_AUTH_ENDPOINT}?{urlencode(params)}"

        logger.info("STEP 4: OAuth URL created")

        return HttpResponseRedirect(auth_url)

    except Exception:
        logger.exception("Google login failed")

        return JsonResponse(
            {"error": "Google login failed"},
            status=500
        )

def google_callback(request):
    """
    Handles Google's redirect after login.
    """

    # 1. Check if the user denied access
    error = request.GET.get("error")

    if error:
        logger.warning(
            "Google OAuth denied by user: %s",
            error
        )
        return redirect("/?auth_error=access_denied")

    # 2. Validate OAuth state
    returned_state = request.GET.get("state")

    expected_state = request.session.pop(
        "oauth_state",
        None
    )

    if (
        not returned_state
        or not expected_state
        or returned_state != expected_state
    ):
        logger.warning("OAuth state mismatch or missing")
        return redirect("/?auth_error=invalid_state")

    # 3. Get authorization code
    code = request.GET.get("code")

    if not code:
        logger.warning(
            "Google callback missing authorization code"
        )
        return redirect("/?auth_error=missing_code")

    # 4. Exchange authorization code for tokens
    token_payload = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    try:
        token_response = requests.post(
            GOOGLE_TOKEN_ENDPOINT,
            data=token_payload,
            timeout=10
        )

        token_response.raise_for_status()

    except requests.RequestException:
        logger.exception(
            "Google token exchange failed"
        )
        return redirect(
            "/?auth_error=token_exchange_failed"
        )

    token_data = token_response.json()

    raw_id_token = token_data.get("id_token")

    if not raw_id_token:
        logger.warning(
            "Google token response missing id_token"
        )
        return redirect(
            "/?auth_error=missing_id_token"
        )

    # 5. Verify Google's ID token
    try:
        id_info = google_id_token.verify_oauth2_token(
            raw_id_token,
            google_requests.Request(),
            GOOGLE_CLIENT_ID,
        )

    except ValueError:
        logger.exception(
            "Google ID token verification failed"
        )
        return redirect(
            "/?auth_error=invalid_id_token"
        )

    # 6. Check that Google verified the email
    if not id_info.get("email_verified", False):
        logger.warning(
            "Google account email not verified"
        )
        return redirect(
            "/?auth_error=email_not_verified"
        )

    # 7. Extract Google user information
    google_id = id_info.get("sub")
    email = id_info.get("email")
    name = id_info.get("name", "")
    picture = id_info.get("picture")

    if not google_id or not email:
        logger.warning(
            "Google token missing required identity fields"
        )
        return redirect(
            "/?auth_error=missing_profile_info"
        )

    # 8. Find user using Google ID
    user = User.objects.filter(
        google_id=google_id
    ).first()

    # 9. If Google ID doesn't exist, check email
    if user is None:

        user = User.objects.filter(
            email=email
        ).first()

        # Existing account
        if user is not None:

            user.google_id = google_id

            if picture and not user.profile_picture:
                user.profile_picture = picture

            user.save()

        # New account
        else:

            username = _generate_unique_username(
                email
            )

            user = User.objects.create(
                username=username,
                email=email,
                google_id=google_id,
                profile_picture=picture,
                first_name=name,
            )

            user.set_unusable_password()
            user.save()

    # 10. Create Django authenticated session
    login(request, user)

    # 11. Redirect after successful login
    return redirect("/auth/success/")

def _generate_unique_username(email):
    """
    Creates a unique username from the email address.
    """

    base = email.split("@")[0]

    username = base

    counter = 1

    while User.objects.filter(
        username=username
    ).exists():

        username = f"{base}{counter}"

        counter += 1

    return username

@login_required(login_url="/")
def auth_success(request):
    context = {
        "email": request.user.email,
        "name": request.user.first_name or request.user.username,
    }

    return render(request, "success.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")