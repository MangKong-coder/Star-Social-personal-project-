from django.urls import urls
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('new/', views.CreateGroup.as_view(), name='group_create'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
]