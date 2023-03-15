from django.urls import path
from . import views

urlpatterns = [
    path("", views.comps, name='companies'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("form/", views.newform, name='form'),

]
