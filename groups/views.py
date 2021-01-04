from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView, DeleteView
from .models import Group, GroupMembers
# Create your views here.

class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group

class GroupDetailView(DetailView):
    model = Group

class GroupListView(ListView):
    model = Group

