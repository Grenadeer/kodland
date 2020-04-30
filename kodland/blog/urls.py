from django.urls import path
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . import views
from .models import Post

urlpatterns = [
    path('post/', ListView.as_view(
        model=Post,
    ), name='post_list'),
    path('post/create/', CreateView.as_view(
        model=Post
    ), name='post_create'),

    path('', RedirectView.as_view(url='/post/'), name='index'),
]
