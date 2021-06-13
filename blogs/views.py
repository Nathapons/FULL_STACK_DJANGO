from django.shortcuts import render
from category.models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'frontend/index.html', {'categories' : categories})