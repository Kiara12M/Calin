from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from Usuarios.models import CustomUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, allow_null=True, allow_blank=True, required=True)
    password = serializers.CharField(max_length=10, allow_null=True, allow_blank=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Debes ingresar el email y la contraseña")

        if not CustomUser.check_password(password):
            raise serializers.ValidationError("Las credenciales no son correctamente")

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("Pon la información correctamente")

        #Para buscar un usuario
        user= None
        if email:
            user = CustomUser.objects.filter(email=email).first()
            if not user:
                raise serializers.ValidationError("No existe un usuario con ese email.")


        tokens = RefreshToken.for_user(user)
        tokens["id"] = user.id
        tokens["nombre"] = user.nombre

        return {
            "ok": True,
            "usuario": {
                "id": user.id,
                "nombre": user.nombre,
                "email": user.email,
            },
            "tokens": {
                "refresh": str(tokens),
                "access": str(tokens.access_token),
            }
        }