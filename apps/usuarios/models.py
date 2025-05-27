from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()

class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Ususarios'
        ordering =['id']

def __str__(self):
    return self.first_name