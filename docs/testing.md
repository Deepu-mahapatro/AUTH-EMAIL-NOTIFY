# AuthNotify — Testing Documentation

## 1. Testing Overview

AuthNotify was tested through the web interface and authentication endpoints during development.

The main goal was to verify the Google OAuth authentication flow, OAuth callback handling, Django session management, authentication success, logout functionality, and environment configuration.

---

## 2. Authentication Tests

| Test                          | Expected Result                 |
| ----------------------------- | ------------------------------- |
| Open authentication page      | Page loads successfully         |
| Google Login button           | Authentication flow starts      |
| Google account authentication | User authenticated by Google    |
| User authorization            | Authorization accepted          |
| OAuth redirect                | User redirected to callback     |
| OAuth callback                | Callback processed successfully |
| Authentication success        | User redirected to success page |

Example:

```text
Open Authentication Page    → Page Loaded
Click Google Login          → Redirected to Google
Google Authentication       → Authentication Successful
OAuth Callback              → Callback Processed
Success Page                → Displayed
```

---

## 3. OAuth Callback Tests

| Test                     | Expected Result           |
| ------------------------ | ------------------------- |
| Valid OAuth callback     | Authentication successful |
| Valid authorization code | Code processed            |
| Invalid callback request | Authentication rejected   |
| Missing OAuth parameters | Request handled safely    |
| Invalid OAuth state      | Authentication rejected   |

---

## 4. Session Tests

| Test                      | Expected Result                     |
| ------------------------- | ----------------------------------- |
| Successful authentication | Django session created              |
| Access after login        | Authenticated user recognized       |
| Logout                    | Session terminated                  |
| Access after logout       | User no longer authenticated        |
| Session expiration        | User required to authenticate again |

---

## 5. API Tests

The following authentication endpoints were tested during development:

```text
GET  /auth/google/login/
GET  /auth/google/callback/
GET  /auth/success/
GET  /auth/logout/
```

The Google login endpoint was tested through the browser because it initiates a browser-based OAuth redirect to Google.

The callback endpoint was tested as part of the complete Google OAuth authentication flow.

---

## 6. Authentication Success Test

The successful Google authentication flow was tested from the initial login request through the OAuth callback.

Expected result:

```text
Google Authentication
        ↓
OAuth Callback
        ↓
Django Authentication
        ↓
Session Created
        ↓
Authentication Success
```

The user was successfully redirected to the authentication success page after completing Google authentication.

---

## 7. Security Tests

The following security features were tested:

```text
✓ Google OAuth authentication
✓ OAuth state validation
✓ Backend authentication processing
✓ Django session management
✓ Secure OAuth credential handling
✓ Environment variable protection
✓ .env exclusion from Git
✓ Logout/session termination
✓ Authentication error handling
```

Sensitive Google OAuth credentials were kept outside the source code using environment variables.

---

## 8. Final Testing Status

The main AuthNotify authentication workflow was tested successfully.

```text
✓ Authentication page
✓ Google Login
✓ Google OAuth redirect
✓ Google account authentication
✓ OAuth authorization
✓ OAuth callback
✓ Django authentication
✓ Session creation
✓ Authentication success
✓ Logout
✓ Session termination
✓ Authentication error handling
✓ Environment variable configuration
```

The complete authentication flow was successfully tested from Google Login through OAuth callback, Django session creation, authentication success, and logout.

---

## 9. Testing Tools

Web Browser

Postman

Django Development Server

Google OAuth 2.0

Django Authentication & Session Framework
