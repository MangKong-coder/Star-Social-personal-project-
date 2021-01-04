from django.urls import path, re_path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('new/', views.PostCreate.as_view(), name='post_create'),
    path("by/<username>/",views.UserPost.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.PostDelete.as_view(),name="delete"),
]