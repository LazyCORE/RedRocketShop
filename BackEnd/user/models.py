from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    __tablename__ = 'user_profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField("Ім'я", max_length=20, default="Користувач", help_text="Введіть своє ім'я")
    last_name = models.CharField("Прізвище", max_length=20, help_text="Введіть своє прізвище")

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('user', kwargs={"user_id": self.pk})
