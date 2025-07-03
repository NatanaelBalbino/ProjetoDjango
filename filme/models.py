from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("MUSICA", "Música"),
    ("PROGRAMACAO", "Programação"),
    ("EXERCICIOS", "Exercícios"),
)


# Create Filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    views = models.IntegerField(default=0)
    data_de_criacao = models.DateTimeField(default=timezone.now

    def __str__(self):
        return self.titulo


# Create Episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
