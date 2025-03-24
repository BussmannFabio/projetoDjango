from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = ['id','username', 'password', 'cpf', 'rg', 'endereco', 'sexo']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True}
            }

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            cpf=validated_data['cpf'],
            rg=validated_data['rg'],
            endereco=validated_data['endereco'],
            sexo=validated_data['sexo']
        )

        return user
