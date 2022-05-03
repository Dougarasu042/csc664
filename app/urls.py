from django.urls import include, path
from django.conf.urls import url
from . import views

# url Config
urlpatterns = [
    path('', views.load_front_page, name='home'),
    path('match_image/', views.match_image, name='results'),
]