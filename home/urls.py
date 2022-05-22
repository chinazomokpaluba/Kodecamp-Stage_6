from django.urls import path
from .views import home,about,contact,service

urlpatterns = [
    path("",home),
    path("about/",about),
    path("contact/",contact),
    path("service/",service),
]
