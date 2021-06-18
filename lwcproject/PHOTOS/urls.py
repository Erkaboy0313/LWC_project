from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main , name = 'main'),
    path('cars/', views.cars , name = 'cars'),
    path('books/', views.books , name = 'books'),
    path('design/', views.design , name = 'design'),
    path('code/', views.code , name = 'code'),
    path('<int:id>', views.info , name = 'info'),
    path('search', views.search , name = 'search'),
]