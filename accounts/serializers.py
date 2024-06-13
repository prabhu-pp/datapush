from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ('app_secret_token', 'account_id')
