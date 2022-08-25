from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name = 'dashboard'),
    path('download/', views.download, name = 'download'),
    path('watch/', views.watch, name = 'watch')
]