from django.urls import path

from . import views

urlpatterns = [

    path('', views.menu, name = 'menu'),
    path('newgame/', views.newgame, name = 'new_game')
]