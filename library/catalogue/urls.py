from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="catalogue-home"),
    path('about/', views.about, name="catalogue-about"),
    path('books/', views.books, name="catalogue-books"),
    path('books/<int:id>/', views.show, name="catalogue-show")
]
