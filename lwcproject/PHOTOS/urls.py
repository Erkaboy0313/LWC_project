from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main , name = 'main'),
    path('<int:id>', views.info , name = 'info'),
    path('search', views.search , name = 'search'),
    path('<str:category>' , views.categories , name='categories')
]