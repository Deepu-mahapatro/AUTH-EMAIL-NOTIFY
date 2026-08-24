# AuthNotify — System Architecture

## 1. Overview

AuthNotify is a Django-based Google authentication and notification system.

It connects the frontend, Django backend, Google OAuth 2.0, Django authentication, session management, and database to provide a secure Google-based authentication workflow.

The system allows users to authenticate through their Google account instead of manually creating and managing a separate password.

---

## 2. Architecture

```text
User
  ↓
Frontend
HTML / CSS / JavaScript
  ↓
Django Backend
  ↓
Google Login Endpoint
  ↓
Google OAuth 2.0
  ↓
Google Authentication
  ↓
OAuth Callback
  ↓
Django Authentication
  ↓
Session Creation
  ↓
Authentication Success
  ↓
Authenticated User
```

---

## 3. Main Components

### Frontend

The frontend provides:

* Authentication interface
* Google Login option
* Authentication status
* Success page
* Logout option
* User interaction and navigation

Technologies: HTML, CSS, JavaScript

### Django Backend

The backend handles:

* URL routing
* Google authentication initiation
* OAuth authorization flow
* OAuth callback handling
* Authentication processing
* User session management
* Logout
* Authentication success handling
* Error handling

Technology: Django

### Google OAuth 2.0

Google OAuth 2.0 is used to authenticate users through their Google accounts.

Google handles:

* Google account authentication
* User authorization
* OAuth authorization response
* Redirecting the user to the configured callback URL

### Django Authentication

Django handles the authenticated user inside the application.

It manages:

* User authentication
* Authentication state
* Login session
* Logout
* Authenticated requests

### Django Session

After successful authentication, Django creates a session for the authenticated user.

The session allows the application to recognize the user across subsequent requests.

### Database

The database is used by Django for application data and session-related information.

Depending on the configured database, Django manages the required authentication and session tables.

---

## 4. Authentication Process

```text
1. User opens the authentication page
             ↓
2. User selects "Login with Google"
             ↓
3. Django receives the login request
             ↓
4. Django redirects the user to Google
             ↓
5. Google authenticates the user
             ↓
6. User grants the required permission
             ↓
7. Google redirects to the OAuth callback
             ↓
8. Django receives the OAuth response
             ↓
9. Django processes the authentication response
             ↓
10. User is authenticated
             ↓
11. Django creates an authenticated session
             ↓
12. User is redirected to the success page
```

---

## 5. Security Flow

```text
Google Authentication
       ↓
OAuth Authorization
       ↓
OAuth State Validation
       ↓
OAuth Callback
       ↓
Backend Authentication
       ↓
Django Session
       ↓
Authenticated User
       ↓
Logout / Session Termination
```

These layers help protect the authentication process by delegating account authentication to Google and keeping application authentication state managed by Django.

Sensitive OAuth credentials are stored using environment variables instead of being hardcoded into the application.

The `.env` file is excluded from Git to prevent sensitive credentials from being exposed.

---

## 6. Data Flow

```text
User
 ↓
Django Frontend
 ↓
Google Login Endpoint
 ↓
Google OAuth 2.0
 ├──→ Google Authentication
 │
 └──→ OAuth Callback
          ↓
     Django Backend
          ↓
     Authentication
          ↓
     Django Session
          ↓
     Success Page
```

The frontend communicates with the Django backend.

The Django backend starts the Google OAuth authentication process.

Google handles the user's account authentication and returns the OAuth response to the configured callback endpoint.

Django processes the callback, authenticates the user, creates the session, and redirects the user to the authentication success page.

---

## 7. Result

After successful Google authentication:

```text
Google Authentication
       ↓
OAuth Callback
       ↓
User Authenticated
       ↓
Django Session Created
       ↓
Authentication Success
       ↓
Success Page
```

After logout:

```text
Authenticated User
       ↓
Logout Request
       ↓
Django Session Terminated
       ↓
User Logged Out
```

This completes the AuthNotify Google authentication workflow.
