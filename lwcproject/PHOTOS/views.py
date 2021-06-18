from typing import Text
from django.shortcuts import render
from .forms import Search
from .models import  Category , Photos
# Create your views here.

def main(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})

def categories(response , category):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/categories.html' , {'ls':ls , 'form':form , 'category':category})

def info(response , id):
    ls = Category.objects.all()
    contex = {
        'ls':ls,
        'id':id
    }
    return render(response , 'PHOTOS/info.html' , contex)

def search(response):
    text = ''
    if response.method=="POST":
        form = Search(response.POST)
        if form.is_valid():
            text = response.POST.get('search')
        else:
            print('invalid')
    T = Photos.objects.filter(Title__icontains = text)
    return render(response , 'PHOTOS/search.html' , {'text':text,'T':T})