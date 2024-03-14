from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView, CarDeleteView

app_name = "AppCar"

urlpatterns = [
    path("list/", CarListView.as_view(), name="list"),
    path("create/", CarCreateView.as_view(), name="create"),
    path("detail/<int:pk>", CarDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", CarDeleteView.as_view(), name="delete"),
]
