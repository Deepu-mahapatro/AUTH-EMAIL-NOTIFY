# AuthNotify — API Documentation

## Base URL

```text
http://127.0.0.1:8000
```

## 1. Google Login

Starts the Google OAuth authentication process.

Method: GET

Endpoint:

```text
/auth/google/login/
```

Response:

The user is redirected to Google's OAuth authentication page.

```text
Django Application
       ↓
Google OAuth 2.0
       ↓
Google Login Page
```

The endpoint does not return a normal JSON response because it initiates a browser-based OAuth authentication flow.

---

## 2. Google OAuth Callback

Handles the response returned by Google after the user completes authentication.

Method: GET

Endpoint:

```text
/auth/google/callback/
```

Request:

Google sends the OAuth response to the configured callback URL.

```text
/auth/google/callback/?code=<authorization_code>&state=<state>
```

Response:

After successful authentication, Django processes the OAuth response and redirects the user to the authentication success page.

```text
Google
   ↓
OAuth Callback
   ↓
Django Authentication
   ↓
Authentication Success
```

---

## 3. Authentication Success

Displays the authentication success page after successful Google authentication.

Method: GET

Endpoint:

```text
/auth/success/
```

Response:

The authenticated user is shown the success page.

```text
Authentication Successful
```

This endpoint is accessed after the Google OAuth callback has successfully authenticated the user.

---

## 4. Logout

Logs out the currently authenticated user and terminates the Django session.

Method: GET

Endpoint:

```text
/auth/logout/
```

Response:

The user's Django authentication session is terminated and the user is logged out.

```text
Authenticated User
       ↓
Logout Request
       ↓
Session Terminated
       ↓
User Logged Out
```

---

## Common Error Responses

| Code | Meaning                                      |
| ---- | -------------------------------------------- |
| 400  | Invalid or incomplete authentication request |
| 403  | Authentication or authorization denied       |
| 404  | Authentication endpoint not found            |
| 500  | Server-side authentication error             |
| 502  | OAuth provider communication problem         |

---

## Authentication Flow

```text
Google Login
   ↓
Google Authentication
   ↓
User Authorization
   ↓
OAuth Callback
   ↓
Django Authentication
   ↓
Session Created
   ↓
Authentication Success
```

The API handles the complete Google OAuth authentication process between the frontend, Django backend, Google OAuth service, and Django session system.