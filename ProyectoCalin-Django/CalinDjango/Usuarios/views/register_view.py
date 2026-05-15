from rest_framework import generics, status
from rest_framework.response import Response
from Usuarios.serializers.register_serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
                "message": "Usuario creado exitosamente. Ahora puedes iniciar sesión."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
