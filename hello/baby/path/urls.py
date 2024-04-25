from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("about", views.about_me),
    # path("about/", views.about_me),
    # path("admin/", admin.site.urls),
]
