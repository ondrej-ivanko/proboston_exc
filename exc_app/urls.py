from django.urls import path
from exc_app import views


app_name = "exc_app"
urlpatterns = [path("user-forms/", views.user_form, name="user_form")]
