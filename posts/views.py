from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
