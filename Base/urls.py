from django.urls import path
from . import views

urlpatterns = [
	path("", views.add_to_db, name = "home"),

   ]