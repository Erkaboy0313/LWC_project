from typing import Text
from django.shortcuts import render
from .forms import Search
from .models import  Category
# Create your views here.

def main(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})

def cars(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})

def books(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})

def design(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})
def code(response):
    ls = Category.objects.all()
    form = Search()
    return render(response , 'PHOTOS/index.html' , {'ls':ls,'form':form})
def info(response , id):
    ls = Category.objects.all()
    contex = {
        'ls':ls,
        'id':id
    }
    return render(response , 'PHOTOS/info.html' , contex)

def search(response):
    text = ''
    ls = Category.objects.all()
    if response.method=="POST":
        form = Search(response.POST)
        if form.is_valid():
            text = response.POST.get('search')
        # text = 'Harry'
        else:
            print('invalid')
    return render(response , 'PHOTOS/search.html' , {'text':text,'ls':ls})