from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .models import Blog
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog List"
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog Detail"
        return context


class BlogCreateView(CreateView):
    model = Blog
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog Form"
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("AppBlog:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog Delete"
        return context
