from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import LivroFilter 

# Classe para listar e criar livros
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter  # Adiciona o filtro personalizado
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)  # Define os filtros
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em', 'categoria__nome']  # Campos que podem ser ordenados
    search_fields = ['titulo', 'autor__nome', 'categoria__nome']  # Campos que podem ser pesquisados

# Classe para detalhar, atualizar e deletar um livro específico
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()  # Consulta todos os livros
    serializer_class = LivroSerializer  # Define o serializer a ser usado
