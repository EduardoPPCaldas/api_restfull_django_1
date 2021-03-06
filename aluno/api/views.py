from rest_framework import viewsets
from aluno.models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
  queryset = Aluno.objects.all().filter(ativo = True)
  serializer_class = AlunoSerializer
