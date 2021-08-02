from django.urls import path , include
from rest_framework import routers
from .views import AlunoViewSet

router = routers.DefaultRouter()

router.register('aluno', AlunoViewSet)

urlpatterns = [
  path('', include(router.urls))
]