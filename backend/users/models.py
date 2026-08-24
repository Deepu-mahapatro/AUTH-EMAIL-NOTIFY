from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model. Extends Django's built-in AbstractUser
    so we get username/password/auth for free, while adding
    fields Google OAuth will need later.
    """

    # Used as the primary identity field once Google login exists
    email = models.EmailField(unique=True)

    # Populated only after Google OAuth is implemented (Phase 2)
    google_id = models.CharField(max_length=255, blank=True, null=True, unique=True)

    # Populated from Google profile data later
    profile_picture = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email or self.username
