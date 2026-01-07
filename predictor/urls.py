from django.urls import path
from . import views

urlpatterns = [
    path("app/", views.predict_view,name="predict"),
]
