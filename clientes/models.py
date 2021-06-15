from django.db import models


class Cliente(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Não definido')
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email =  models.EmailField(null=False, blank= False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.nome