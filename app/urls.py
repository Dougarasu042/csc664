from django.urls import path
from . import views

# url Config
urlpatterns = [
    path('hello/', views.say_hello)
]