from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'nombre', 'apellidos', 'email', 'password')
        extra_kwargs = {
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data.get('nombre', ''),
            apellidos=validated_data.get('apellidos', '')
        )
        return user
