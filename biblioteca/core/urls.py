from django.urls import path
from core.views import LivroList, LivroDetail

urlpatterns = [
    path('', LivroList.as_view(), name='livros-list-create'),  
    path('<int:pk>/', LivroDetail.as_view(), name='livro-detail'), 
]
