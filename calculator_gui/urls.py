from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("section_b", views.section_b, name="section b"),
    path("hoffman", views.hoffman, name="Hoffman"),
    path("julian", views.julian, name="Julian"),
    path("lst", views.lst, name="LST"),
]
