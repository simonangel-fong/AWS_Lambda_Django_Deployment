from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView

app_name = "AppBlog"

urlpatterns = [
    path("list/", BlogListView.as_view(), name="list"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
]
