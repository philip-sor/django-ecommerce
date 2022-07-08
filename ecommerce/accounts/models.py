from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.mail import send_mail


# Create your models here.


class CustomAccountManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email must be provided'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    country = CountryField()
    phone_number = models.TextField(max_length=15, blank=True)
    postcode = models.CharField(max_length=12, blank=True)
    town_city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    post_office_name = models.CharField(max_length=100, blank=True)
    post_office_code = models.CharField(max_length=20, blank=True)

    about = models.TextField(max_length=500, blank=True)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def email_user(self, subject, message):
        import smtplib
        project_email = "yourslaveyourbitc4@gmail.com"
        project_password = "abcd1234()"
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=project_email, password=project_password)
            connection.sendmail(project_email, self.email, msg=f"Subject:{subject}\n\n{message}")
        
