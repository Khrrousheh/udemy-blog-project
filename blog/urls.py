from django.urls import path
from . import views


urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('posts', views.get_all_post, name='posts-page'),
    path("post/<slug:slug>", views.get_post, name='post-detail-page'),
]
