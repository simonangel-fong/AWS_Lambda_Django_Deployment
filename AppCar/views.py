from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .models import Car
from django.urls import reverse_lazy


class CarListView(ListView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Car List"
        return context


class CarDetailView(DetailView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Car Detail"
        return context


class CarCreateView(CreateView):
    model = Car
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Car Form"
        return context


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("AppCar:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Car Delete"
        return context
