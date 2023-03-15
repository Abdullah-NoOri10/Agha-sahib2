from django.urls import path
from . import views

urlpatterns = [
    path("", views.comps, name='companies'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("form/", views.create_product, name='create-product'),
    path("login/", views.login, name='login'),
    path("error/", views.error_page, name='error'),

]
