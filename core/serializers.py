from dataclasses import fields
from djoser.serializers import UserCreateSerializer as BaseCreateUserSerializer

class CreateUserSerializer(BaseCreateUserSerializer):
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ['id', 'username','first_name', 'last_name', 'email', 'password']