from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models
from rest_framework.authtoken.models import Token


class CopyData(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, default="")
    date = models.CharField(max_length=40, default="nodate")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class CopyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyData
        fields = ('content', 'date', 'user')


# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
