from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, null=True)
    password = models.CharField(max_length=255)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.username} {self.email}"
