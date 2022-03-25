from django.urls import include, path
from django.conf.urls import url
from . import views

# url Config
urlpatterns = [
    path('', views.load_front_page),
    path('match_image/', views.match_image),
]