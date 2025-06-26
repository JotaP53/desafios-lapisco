from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Livro, Autor
from .serializers import LivroSerializer, AutorSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def criar_livro(request):
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def listar_livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return JsonResponse(serializer.data, safe=False)
