from rest_framework import serializers
from .models import Livro, Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'data_nascimento', 'biografia']


class LivroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True)
    
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'descricao', 'data_publicacao', 'autores']
