from django.db import models
from django.contrib.auth.models import User
from django.forms import FileField, ModelForm


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

