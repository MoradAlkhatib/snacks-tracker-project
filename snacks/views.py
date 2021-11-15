from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from snacks.models import Snack


class HomeView(ListView):
    template_name = 'home.html'
    model = Snack


class SnackListDetail(DetailView):
    template_name = "list_detail.html"
    model = Snack
    context_object_name = "snack_object"