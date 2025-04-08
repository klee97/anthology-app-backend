from django.urls import path

from . import views

urlpatterns = [
    path("", views.stories_list, name="stories_list"),
    path('<str:id>', views.detail, name='detail'),
    path('story-evals/<str:username>/', views.reader_story_evals, name='story-evals'),
]
