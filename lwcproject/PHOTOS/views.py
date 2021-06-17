from django.shortcuts import render

from .models import  Category
# Create your views here.

def main(response):
    ls = Category.objects.all()
    return render(response , 'PHOTOS/layout.html' , {'ls':ls})