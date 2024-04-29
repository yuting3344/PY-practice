from django.urls import path
from . import views

app_name = "postes"
urlpatterns = [
    path("", views.home, name="index"),
    path("new", views.new, name="new"),
    path("add", views.create, name="add"),
    path("<id>/edit", views.edit, name="edit"),
    path("<id>/delete", views.delete, name="delete"),
    path("<id>", views.show, name="show"),
]
