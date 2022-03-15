from djoser.serializers import UserCreateSerializer as BaseCreateUserSerializer, UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('id','username', 'email', 'first_name', 'last_name', 'is_staff')


class CreateUserSerializer(BaseCreateUserSerializer):
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ['id', 'username','first_name', 'last_name', 'email', 'password']