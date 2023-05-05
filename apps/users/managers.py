from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        """
        Validates if an email address is valid or not.
        """
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValueError from e(_("You must provide a valid email address"))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        """
        Creates a user with required fields such as username, first name, last name, email,
        and password, and sets default values for optional fields.
        """
        if not username:
            raise ValueError(_("Users must submit a username"))

        if not first_name:
            raise ValueError(_("Users must submit a first name"))

        if not last_name:
            raise ValueError(_("Users must submit a last name"))

        if not email:
            raise ValueError(_("Base User Account: An email address is required"))

        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        """
        Creates a superuser with specific attributes and raises errors if certain
        conditions are not met.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Supersusers must have is_staff=True"))

        if extra_fields.get("is_supersuser") is not True:
            raise ValueError(_("Supersusers must have is_supersuser=True"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if not email:
            raise ValueError(_("Admin Account: An email address is required"))

        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        user.save(using=self._db)
        return user
