from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("section_b/1", views.section_b_1, name="section b 1"),
    path("section_b/2", views.section_b_2, name="section b 1"),
    path("section_b/3", views.section_b_3, name="section b 1"),
    path("hoffman", views.hoffman, name="Hoffman"),
    path("julian", views.julian, name="Julian"),
    path("lst", views.lst, name="LST"),
    path("section_a", views.section_a, name="section_a"),
    path("kepler_eqn", views.kepler_eqn, name="kepler_eqn"),
    path("kepler_hyp", views.kepler_hyp, name="kepler_hyp"),
]
