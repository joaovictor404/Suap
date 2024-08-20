from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    data_nascimento = models.DateField()
    image = models.ImageField(upload_to='alunos',null=True,blank=True)

    def __str__(self):
        return self.nome