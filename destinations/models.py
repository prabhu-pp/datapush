from django.db import models
from accounts.models import Account

class Destination(models.Model):
    HTTP_METHOD_CHOICES = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
    ]

    account = models.ForeignKey(Account, related_name='destinations', on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=4, choices=HTTP_METHOD_CHOICES)
    headers = models.JSONField()

    class Meta:
        unique_together = ('account', 'url')
