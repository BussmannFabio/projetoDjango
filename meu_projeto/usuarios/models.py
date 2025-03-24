from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=14, unique= False)
    rg = models.CharField(max_length=12, unique= False)
    endereco = models.TextField()
    sexo = models.CharField(
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Feminino')]
    )

    def __str__(self):
        return self.username