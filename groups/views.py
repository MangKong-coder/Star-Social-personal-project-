from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView, DeleteView, RedirectView
from groups.models import Group, GroupMembers
# Create your views here.

class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group

class GroupDetailView(DetailView):
    model = Group

class SingleGroup(DetailView):
    model = Group

class GroupListView(ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('get')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMembers.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member!')
        else:
            messages.success(self.request,'You are now a member')

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('get')})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMembers.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupMembers.DoesNotExist:
            messages.warning(self.request,'Sorry you are\'t in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')
        return super().get(request, *args, **kwargs)


