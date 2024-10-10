from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro
from datetime import date

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        # Criação de categorias
        categoria_ficcao = Categoria.objects.get_or_create(nome="Ficção")[0]
        categoria_misterio = Categoria.objects.get_or_create(nome="Mistério")[0]
        categoria_fantasia = Categoria.objects.get_or_create(nome="Fantasia")[0]

        # Criação de autores
        autor_asimov = Autor.objects.get_or_create(nome="Isaac Asimov")[0]
        autor_tolkien = Autor.objects.get_or_create(nome="J.R.R. Tolkien")[0]
        autor_christie = Autor.objects.get_or_create(nome="Agatha Christie")[0]

        # Criação de livros
        Livro.objects.get_or_create(
            titulo="Fundação", 
            autor=autor_asimov, 
            categoria=categoria_ficcao, 
            publicado_em=date(1951, 6, 1)
        )
        Livro.objects.get_or_create(
            titulo="O Hobbit", 
            autor=autor_tolkien, 
            categoria=categoria_fantasia, 
            publicado_em=date(1937, 9, 21)
        )
        Livro.objects.get_or_create(
            titulo="Assassinato no Expresso do Oriente", 
            autor=autor_christie, 
            categoria=categoria_misterio, 
            publicado_em=date(1934, 1, 1)
        )

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
