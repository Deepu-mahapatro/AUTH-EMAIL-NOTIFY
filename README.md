# AuthNotify — Google Authentication & Notification System

AuthNotify is a Django-based authentication system that allows users to securely authenticate using their Google account through **Google OAuth 2.0**.

The project demonstrates a complete OAuth authentication workflow, including Google authorization, callback handling, user authentication, Django session management, and authentication success handling.

Built for **educational and portfolio purposes**.

## 🌐 Live Demo

**Live Application:**  
https://django-google-authentication.onrender.com/

**Source Code:**  
<https://github.com/Deepu-mahapatro/SECUREAUTH-EMAIL-OTP.git>


## 📌 Overview


AuthNotify provides a simple Google-based authentication workflow.

Users start the login process from the Django application and are redirected to Google for authentication. After successful authentication, Google redirects the user back to the Django callback endpoint.

Django processes the OAuth response, authenticates the user, creates a session, and redirects the user to the authentication success page.

The project uses Django, Google OAuth 2.0, Django authentication, session management, and environment-based configuration.


## ✨ Features


* Google OAuth 2.0 authentication
* Google Sign-In integration
* OAuth authorization flow
* OAuth callback handling
* Automatic user authentication
* Django session-based authentication
* Authentication success page
* User login state management
* User logout
* OAuth state validation
* Secure OAuth credential handling
* Environment variable configuration
* `.env` credential protection
* Backend authentication processing
* Authentication error handling
* Session management
* Responsive authentication interface
* Browser-based authentication testing


## 🔐 Authentication Flow


```text
User
     ↓
Open Authentication Page
     ↓
Click "Login with Google"
     ↓
Django Login Endpoint
     ↓
Redirect to Google
     ↓
Google Authentication
     ↓
User Grants Permission
     ↓
Google OAuth Callback
     ↓
Django Processes OAuth Response
     ↓
Authenticate User
     ↓
Create Django Session
     ↓
Authentication Success
```

### Google OAuth Flow

```text
Browser
    │
    ▼
Django Application
    │
    ▼
/auth/google/login/
    │
    ▼
Google OAuth 2.0
    │
    ▼
Google Login
    │
    ▼
User Authorization
    │
    ▼
/auth/google/callback/
    │
    ▼
OAuth Response
    │
    ▼
Django Authentication
    │
    ▼
Session Created
    │
    ▼
/auth/success/
```

The authentication process starts when the user selects Google Login.

Django redirects the user to Google's OAuth authorization page.

After successful authentication, Google sends the authorization response back to the configured callback URL.

Django processes the response and authenticates the user.

A Django session is then created for the authenticated user.

---

## 🛠️ Technology Stack

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| Python                | Programming Language           |
| Django 6.1            | Backend Web Framework          |
| HTML5                 | Frontend                       |
| CSS3                  | Styling                        |
| JavaScript            | Frontend Logic                 |
| Google OAuth 2.0      | User Authentication            |
| Django Authentication | User Authentication Management |
| Django Sessions       | Session Management             |
| PostgreSQL   | Database   |
| python-dotenv         | Environment Configuration      |
| Postman               | API Testing                    |
| Git & GitHub          | Version Control                |

---

## 📂 Project Structure

```text
AUTHENTICATION-NOTIFICATION-PROJECT/
│
├── README.md
├── .gitignore
│
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── .env.example
    │
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── authentication/
    │   ├── __init__.py
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    │
    ├── templates/
    │   ├── index.html
    │   └── success.html
    │
    └── static/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
```

The project is organized into a Django backend, authentication application, templates, static files, and configuration files.

The `.env` file is used locally for sensitive configuration and is excluded from Git.

---

## 🔗 API Endpoints

### Google Login

```text
GET /auth/google/login/
```

Starts the Google OAuth authentication process.

The endpoint redirects the user to Google's authentication page.

---

### Google OAuth Callback

```text
GET /auth/google/callback/
```

Handles the callback sent by Google after the user completes authentication.

The callback processes the OAuth response and authenticates the user.

---

### Authentication Success

```text
GET /auth/success/
```

Displays the authentication success page after successful Google authentication.

---

### Logout

```text
GET /auth/logout/
```

Logs out the currently authenticated user and terminates the Django authentication session.

---

## 🛡️ Security Features

* Google OAuth 2.0 authentication
* OAuth state validation
* Server-side authentication processing
* Django session-based authentication
* Environment-based credential management
* Google Client ID stored through environment variables
* Google Client Secret stored through environment variables
* `.env` excluded from Git
* No OAuth secrets hardcoded in source code
* Secure callback handling
* Backend authentication validation
* Session termination during logout
* Safe authentication error handling

Google OAuth credentials should never be stored directly inside the source code.

Sensitive credentials are stored using environment variables.

```text
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
```

The actual `.env` file must never be uploaded to GitHub.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Open the Backend

```bash
cd AUTHENTICATION-NOTIFICATION-PROJECT/backend
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

Depending on the final Django configuration, additional environment variables may include:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

For local development, configure the Google OAuth redirect URI as:

```text
http://127.0.0.1:8000/auth/google/callback/
```

Never upload your actual `.env` file or Google Client Secret to GitHub.

---

## 🗄️ Database Setup

The project uses Django's database and authentication/session framework.

After configuring the environment variables, run:

```bash
python manage.py makemigrations
```

Then apply the migrations:

```bash
python manage.py migrate
```

Django creates the required database tables used by the application, including authentication and session-related tables.

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The authentication page will be displayed.

Click the Google authentication option to begin the OAuth login process.

The authentication flow will proceed through:

```text
http://127.0.0.1:8000/auth/google/login/
```

Google will authenticate the user and redirect back to:

```text
http://127.0.0.1:8000/auth/google/callback/
```

After successful authentication, the user is redirected to the success page.

---

## 🧪 Testing

The Google authentication workflow was tested using the browser and API testing tools during development.

Tested cases include:

* Application startup
* Authentication page
* Google login button
* Google OAuth redirect
* Google account authentication
* OAuth authorization
* OAuth callback
* Successful authentication
* Django session creation
* Authentication success page
* User logout
* Session termination
* Invalid authentication flow
* Invalid callback handling
* Authentication error handling
* Environment variable configuration
* OAuth credential configuration
* Browser compatibility testing

### Browser Authentication Test

The main authentication workflow was tested using:

```text
http://127.0.0.1:8000/
```

Login request:

```text
GET /auth/google/login/
```

Google authentication:

```text
Google OAuth 2.0
```

Callback:

```text
GET /auth/google/callback/
```

Success:

```text
GET /auth/success/
```

Logout:

```text
GET /auth/logout/
```

The complete authentication flow was successfully tested from login through Google authentication, callback processing, session creation, and authentication success.

---

## 🚀 Future Improvements

* Email/password authentication
* Email verification
* JWT authentication
* Refresh token handling
* Role-based access control
* User profile management
* Password reset
* Additional OAuth providers
* GitHub OAuth authentication
* Microsoft OAuth authentication
* Multi-factor authentication
* Automated authentication tests
* API documentation using Swagger/OpenAPI
* Rate limiting
* Production deployment
* HTTPS configuration
* Monitoring and logging
* Authentication activity tracking

---

## 🎓 Educational & Portfolio Purpose

This project demonstrates practical experience with:

* Django backend development
* Google OAuth 2.0
* Third-party authentication integration
* OAuth authorization flow
* OAuth callback handling
* Django authentication framework
* Session management
* Environment-based configuration
* Secure credential management
* Backend development
* API endpoint development
* Authentication testing
* Browser-based application testing
* Git and GitHub

The project is designed to demonstrate practical understanding of **modern authentication workflows and secure Django application development**.

---

## 📄 License

This project is licensed for educational and portfolio purposes.


