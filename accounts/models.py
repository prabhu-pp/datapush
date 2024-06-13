from django.db import models
import uuid
import secrets

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=32, unique=True, editable=False)
    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = secrets.token_hex(16)
        super().save(*args, **kwargs)

