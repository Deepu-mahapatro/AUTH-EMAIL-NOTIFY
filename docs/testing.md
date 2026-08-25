# AuthNotify — Testing Documentation

## 1. Testing Overview

AuthNotify was tested through the web interface and authentication endpoints during development and after production deployment.

The main goal was to verify the Google OAuth authentication flow, OAuth callback handling, Django session management, authentication success, logout functionality, PostgreSQL database connectivity, static file handling, production deployment, and environment configuration.

---

## 2. Authentication Tests

| Test                          | Expected Result                  |
| ----------------------------- | -------------------------------- |
| Open authentication page      | Page loads successfully          |
| Google Login button           | Authentication flow starts       |
| Google account authentication | User authenticated by Google     |
| User authorization            | Authorization accepted           |
| OAuth redirect                | User redirected to callback      |
| OAuth callback                | Callback processed successfully  |
| Authentication success        | User redirected to success page  |

Example:

```text
Open Authentication Page    → Page Loaded

Click Google Login          → Redirected to Google

Google Authentication       → Authentication Successful

OAuth Callback              → Callback Processed

Success Page                → Displayed
3. OAuth Callback Tests
Test	Expected Result
Valid OAuth callback	Authentication successful
Valid authorization code	Code processed
Invalid callback request	Authentication rejected
Missing OAuth parameters	Request handled safely
Invalid OAuth state	Authentication rejected
Invalid ID token	Authentication rejected
Unverified Google email	Authentication rejected
4. Session Tests
Test	Expected Result
Successful authentication	Django session created
Access after login	Authenticated user recognized
Logout	Session terminated
Access after logout	User no longer authenticated
Session expiration	User required to authenticate again
5. API Tests

The following authentication endpoints were tested during development:

GET  /auth/google/login/

GET  /auth/google/callback/

GET  /auth/success/

GET  /auth/logout/

The Google login endpoint was tested through the browser because it initiates a browser-based OAuth redirect to Google.

The callback endpoint was tested as part of the complete Google OAuth authentication flow.

The authentication success endpoint was tested after successful Google authentication.

The logout endpoint was tested to verify Django session termination.

6. Authentication Success Test

The successful Google authentication flow was tested from the initial login request through the OAuth callback.

Expected result:

Google Authentication

        ↓

OAuth Callback

        ↓

Django Authentication

        ↓

Session Created

        ↓

Authentication Success

The user was successfully redirected to the authentication success page after completing Google authentication.

7. Security Tests

The following security features were tested:

✓ Google OAuth authentication

✓ OAuth state validation

✓ Google ID token verification

✓ Verified Google email checking

✓ Backend authentication processing

✓ Django session management

✓ Secure OAuth credential handling

✓ Environment variable protection

✓ .env exclusion from Git

✓ Logout/session termination

✓ Authentication error handling

Sensitive Google OAuth credentials were kept outside the source code using environment variables.

8. Database Tests

The production application uses PostgreSQL.

The following database functionality was verified:

✓ PostgreSQL database connection

✓ Django database configuration

✓ Database migrations

✓ User data storage

✓ Django session data storage

✓ Authentication-related database operations

The production PostgreSQL database is hosted on Render.

9. Static File Tests

Static files were tested after production deployment.

The following functionality was verified:

✓ CSS files load correctly

✓ JavaScript files load correctly

✓ Static files collected successfully

✓ WhiteNoise static file serving

✓ Static files accessible from production

Static files are collected during deployment using Django's collectstatic command and served through WhiteNoise.

10. Production Deployment Tests

The deployed application was tested on the Render production environment.

Production URL:

https://django-google-authentication.onrender.com/

The following production functionality was verified:

✓ Application loads successfully

✓ Production HTTPS connection

✓ Authentication page loads

✓ Static files load correctly

✓ Google Login works

✓ Google OAuth redirect works

✓ Google account authentication works

✓ OAuth callback works

✓ Django authentication works

✓ PostgreSQL connection works

✓ Django session creation works

✓ Authentication success page loads

✓ Logout works

✓ Session termination works

Production Google OAuth callback:

https://django-google-authentication.onrender.com/auth/google/callback/
11. Final Testing Status

The main AuthNotify authentication workflow was tested successfully.

✓ Authentication page

✓ Google Login

✓ Google OAuth redirect

✓ Google account authentication

✓ OAuth authorization

✓ OAuth callback

✓ OAuth state validation

✓ Google ID token verification

✓ Django authentication

✓ PostgreSQL database connection

✓ Session creation

✓ Authentication success

✓ Static file loading

✓ Production deployment

✓ Logout

✓ Session termination

✓ Authentication error handling

✓ Environment variable configuration

The complete authentication flow was successfully tested from Google Login through OAuth callback, Django authentication, PostgreSQL database operations, session creation, authentication success, and logout.

12. Testing Tools

Web Browser

Postman

Django Development Server

Google OAuth 2.0

Django Authentication & Session Framework

PostgreSQL

Render

Gunicorn

WhiteNoise