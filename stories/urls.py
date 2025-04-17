from django.urls import path, include
from . import views

urlpatterns = [
    path('stories/', views.stories_list, name="stories_list"),
    path('stories/<str:id>', views.detail, name='detail'),
    path('story-evals/<str:username>/', views.reader_story_evals, name='story-evals'),
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
