from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_stories, name="all_stories"),
    path('<str:id>', views.detail, name='detail')
]