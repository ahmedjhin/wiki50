from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('?q=css/', views.csst, name='csst'),
]
