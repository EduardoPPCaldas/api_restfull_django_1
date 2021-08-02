from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class Aluno(models.Model):
  nome = models.CharField(
    verbose_name="Nome do aluno",
    max_length=200
  )
  profissao = models.CharField(
    verbose_name="Profissão do aluno",
    max_length=200
  )
  ano_nascimento = models.PositiveSmallIntegerField(
    validators= [MaxValueValidator(datetime.now().year) , MinValueValidator(1970)]
  )

  ativo = models.BooleanField(
    verbose_name="O aluno está ativo",
    default=True
  )
  def __str__(self):
      return self.nome