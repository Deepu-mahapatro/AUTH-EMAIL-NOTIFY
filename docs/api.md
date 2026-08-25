# AuthNotify — API Documentation

## Base URLs

### Local Development

```text
http://127.0.0.1:8000
Production
https://django-google-authentication.onrender.com
Live Application
https://django-google-authentication.onrender.com/
1. Google Login

Starts the Google OAuth authentication process.

Method: GET

Endpoint:

/auth/google/login/

Production Endpoint:

https://django-google-authentication.onrender.com/auth/google/login/

Response:

The user is redirected to Google's OAuth authentication page.

Django Application

       ↓

Google OAuth 2.0

       ↓

Google Login Page

The endpoint does not return a normal JSON response because it initiates a browser-based OAuth authentication flow.

2. Google OAuth Callback

Handles the response returned by Google after the user completes authentication.

Method: GET

Endpoint:

/auth/google/callback/

Production Endpoint:

https://django-google-authentication.onrender.com/auth/google/callback/

Request:

Google sends the OAuth response to the configured callback URL.

/auth/google/callback/?code=<authorization_code>&state=<state>

Production Callback URL:

https://django-google-authentication.onrender.com/auth/google/callback/

Response:

After successful authentication, Django processes the OAuth response and redirects the user to the authentication success page.

Google

   ↓

OAuth Callback

   ↓

Django Authentication

   ↓

Authentication Success

During the callback process, Django:

Validates the OAuth state.
Exchanges the authorization code for Google tokens.
Verifies the Google ID token.
Checks that the Google email is verified.
Finds or creates the corresponding user.
Creates a Django authenticated session.
Redirects the user to the authentication success page.
3. Authentication Success

Displays the authentication success page after successful Google authentication.

Method: GET

Endpoint:

/auth/success/

Production Endpoint:

https://django-google-authentication.onrender.com/auth/success/

Response:

The authenticated user is shown the success page.

Authentication Successful

This endpoint is accessed after the Google OAuth callback has successfully authenticated the user.

The endpoint requires an authenticated Django session.

4. Logout

Logs out the currently authenticated user and terminates the Django session.

Method: GET

Endpoint:

/auth/logout/

Production Endpoint:

https://django-google-authentication.onrender.com/auth/logout/

Response:

The user's Django authentication session is terminated and the user is logged out.

Authenticated User

       ↓

Logout Request

       ↓

Session Terminated

       ↓

User Logged Out
Common Error Responses
Code	Meaning
400	Invalid or incomplete authentication request
403	Authentication or authorization denied
404	Authentication endpoint not found
500	Server-side authentication error
502	OAuth provider communication problem
Authentication Flow
Google Login

   ↓

Google Authentication

   ↓

User Authorization

   ↓

OAuth Callback

   ↓

OAuth State Validation

   ↓

Authorization Code Exchange

   ↓

Google ID Token Verification

   ↓

User Creation / Existing User Lookup

   ↓

Django Authentication

   ↓

PostgreSQL Database

   ↓

Session Created

   ↓

Authentication Success

The API handles the complete Google OAuth authentication process between the frontend, Django backend, Google OAuth service, PostgreSQL database, and Django session system.

Production Deployment

The application is deployed using Render.
