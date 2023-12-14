from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import render


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'index.html', context)
