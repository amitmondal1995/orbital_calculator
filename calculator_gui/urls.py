from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("section_b", views.section_b, name="section b"),
]
