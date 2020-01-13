from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.username
