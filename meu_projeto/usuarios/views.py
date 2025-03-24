from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # Permite que qualquer usuário (inclusive não autenticado) possa criar um novo usuário
    permission_classes = [permissions.AllowAny]
