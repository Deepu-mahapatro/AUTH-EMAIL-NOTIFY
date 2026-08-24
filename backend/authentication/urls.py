from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health/', views.health, name='health'),
    path('auth/status/', views.authentication_status, name='auth-status'),
    
      # Google OAuth entry point — redirects browser to Google
    path('auth/google/login/', views.google_login, name='google-login'),

    # Google redirects back here after user consents
    path('auth/google/callback/', views.google_callback, name='google-callback'),
    
    path('auth/success/', views.auth_success, name='auth-success'),
path('auth/logout/', views.logout_view, name='logout'),
]