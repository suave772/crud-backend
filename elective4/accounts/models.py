from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=244, null=True, blank=True)
    password = models.CharField(max_length=244, null=True, blank=True)

    def __str__(self):
        return self.username