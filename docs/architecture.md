# AuthNotify — System Architecture

## 1. Overview

AuthNotify is a Django-based Google authentication and notification system.

It connects the frontend, Django backend, Google OAuth 2.0, Django authentication, session management, and database to provide a secure Google-based authentication workflow.

The system allows users to authenticate through their Google account instead of manually creating and managing a separate password.

The application is deployed in a production environment using Render, Gunicorn, PostgreSQL, and WhiteNoise.

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

OAuth State Validation

  ↓

Google ID Token Verification

  ↓

Django Authentication

  ↓

PostgreSQL Database

  ↓

Session Creation

  ↓

Authentication Success

  ↓

Authenticated User
3. Main Components
Frontend

The frontend provides:

Authentication interface
Google Login option
Authentication status
Success page
Logout option
User interaction and navigation

Technologies: HTML, CSS, JavaScript

Django Backend

The backend handles:

URL routing
Google authentication initiation
OAuth authorization flow
OAuth callback handling
OAuth state validation
Google ID token verification
Authentication processing
User creation and lookup
User session management
Logout
Authentication success handling
Error handling

Technology: Django

Google OAuth 2.0

Google OAuth 2.0 is used to authenticate users through their Google accounts.

Google handles:

Google account authentication
User authorization
OAuth authorization response
Authorization code generation
Redirecting the user to the configured callback URL
Django Authentication

Django handles the authenticated user inside the application.

It manages:

User authentication
Authentication state
Login session
Logout
Authenticated requests
Django Session

After successful authentication, Django creates a session for the authenticated user.

The session allows the application to recognize the user across subsequent requests.

The session data is stored using Django's database-backed session system.

Database

PostgreSQL is used as the production database for the application.

The database is used by Django for application data and session-related information.

Django manages the required authentication and session tables.

The production PostgreSQL database is hosted on Render.

Gunicorn

Gunicorn is used as the production WSGI server.

It runs the Django application in the Render production environment.

Render Web Service

       ↓

Gunicorn

       ↓

Django Application
WhiteNoise

WhiteNoise is used to serve Django static files in the production environment.

Static files are collected during deployment and served through WhiteNoise.

Render

Render provides the production hosting environment for the application.

The deployment uses:

Render Web Service for Django
Render PostgreSQL for the database
Gunicorn for the production WSGI server
Environment variables for sensitive configuration
4. Authentication Process
1. User opens the authentication page

             ↓

2. User selects "Login with Google"

             ↓

3. Django receives the login request

             ↓

4. Django generates a secure OAuth state

             ↓

5. Django stores the OAuth state in the session

             ↓

6. Django redirects the user to Google

             ↓

7. Google authenticates the user

             ↓

8. User grants the required permission

             ↓

9. Google redirects to the OAuth callback

             ↓

10. Django receives the OAuth response

             ↓

11. Django validates the OAuth state

             ↓

12. Django exchanges the authorization code for tokens

             ↓

13. Django verifies the Google ID token

             ↓

14. Django checks that the Google email is verified

             ↓

15. Django finds or creates the corresponding user

             ↓

16. User is authenticated

             ↓

17. Django creates an authenticated session

             ↓

18. User is redirected to the success page
5. Security Flow
Google Authentication

       ↓

OAuth Authorization

       ↓

OAuth State Validation

       ↓

OAuth Callback

       ↓

Authorization Code Exchange

       ↓

Google ID Token Verification

       ↓

Verified Google Email

       ↓

Backend Authentication

       ↓

Django Session

       ↓

Authenticated User

       ↓

Logout / Session Termination

These layers help protect the authentication process by delegating account authentication to Google and keeping application authentication state managed by Django.

OAuth state validation helps protect the authentication callback from invalid or unexpected authentication requests.

Google ID tokens are verified using the configured Google Client ID.

Sensitive OAuth credentials are stored using environment variables instead of being hardcoded into the application.

The .env file is excluded from Git to prevent sensitive credentials from being exposed.

Production environment variables are configured securely through Render.

6. Data Flow
User

↓

Django Frontend

↓

Google Login Endpoint

↓

Generate OAuth State

↓

Google OAuth 2.0

 ├──→ Google Authentication

 │

 └──→ OAuth Callback

          ↓

     OAuth State Validation

          ↓

     Authorization Code Exchange

          ↓

     Google ID Token Verification

          ↓

     Django Backend

          ↓

     User Lookup / Creation

          ↓

     PostgreSQL Database

          ↓

     Authentication

          ↓

     Django Session

          ↓

     Success Page

The frontend communicates with the Django backend.

The Django backend starts the Google OAuth authentication process.

Google handles the user's account authentication and returns the OAuth response to the configured callback endpoint.

Django processes the callback, validates the OAuth state, exchanges the authorization code for tokens, verifies the Google ID token, and checks the user's verified email.

Django then authenticates the user, creates or updates the corresponding user record, creates the session, and redirects the user to the authentication success page.

PostgreSQL stores the required application, user, and session-related data.

7. Production Architecture

The application is deployed using Render.

User Browser

      ↓

Render Web Service

      ↓

Gunicorn

      ↓

Django Application

      ├──────────────→ Google OAuth 2.0
      │
      ↓
PostgreSQL Database

      ↓

Django Session

      ↓

Authentication Success
Production URL
https://django-google-authentication.onrender.com/
Production Google OAuth Callback
https://django-google-authentication.onrender.com/auth/google/callback/
Production Static Files
Django Static Files

       ↓

collectstatic

       ↓

WhiteNoise

       ↓

Production Browser
8. Deployment Flow
Developer

   ↓

VS Code

   ↓

Git

   ↓

GitHub

   ↓

Render

   ↓

Install Dependencies

   ↓

Run Database Migrations

   ↓

Collect Static Files

   ↓

Gunicorn

   ↓

Django Application

   ↓

Render PostgreSQL

   ↓

Live Application

The application source code is maintained in GitHub.

Render deploys the application from the GitHub repository.

During deployment, Django dependencies are installed, database migrations are applied, and static files are collected.

Gunicorn then starts the Django production application.

9. Result

After successful Google authentication:

Google Authentication

       ↓

OAuth Callback

       ↓

OAuth State Validation

       ↓

Google ID Token Verification

       ↓

User Authenticated

       ↓

PostgreSQL User Data

       ↓

Django Session Created

       ↓

Authentication Success

       ↓

Success Page

After logout:

Authenticated User

       ↓

Logout Request

       ↓

Django Session Terminated

       ↓

User Logged Out

This completes the AuthNotify Google authentication workflow.