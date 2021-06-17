from django.shortcuts import render

from .models import  Category
# Create your views here.

def main(response):
    ls = Category.objects.all()
    return render(response , 'PHOTOS/index.html' , {'ls':ls})
def cars(response):
    ls = Category.objects.all()
    ls1 = Category.objects.get(id =1)
    print(ls1.photos_set.get(id=8))
    return render(response , 'PHOTOS/cars.html' , {'ls':ls})
def books(response):
    ls = Category.objects.all()
    return render(response , 'PHOTOS/books.html' , {'ls':ls})
def design(response):
    ls = Category.objects.all()
    return render(response , 'PHOTOS/design.html' , {'ls':ls})
def code(response):
    ls = Category.objects.all()
    return render(response , 'PHOTOS/code.html' , {'ls':ls})
def info(response , id):
    ls = Category.objects.all()
    contex = {
        'ls':ls,
        'id':id
    }
    return render(response , 'PHOTOS/info.html' , contex)
