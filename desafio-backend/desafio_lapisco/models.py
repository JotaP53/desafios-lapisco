from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateField()
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo
