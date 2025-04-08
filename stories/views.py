from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Story
from .models import StoryEval, Reader
from .serializers import StorySerializer, UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)

def detail(request, id):
  story = Story.objects.get(id=id)
  story_json = serialize('json', [story])
  return JsonResponse(story_json, safe=False)

def stories_list(request):
    """
    List all stories
    """
    if request.method == 'GET':
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return JsonResponse(serializer.data, safe=False)


def reader_story_evals(request, username):
    user = get_object_or_404(User, username=username)  # Fetch the user by ID
    reader = get_object_or_404(Reader, user=user)  # Get the Reader profile

    # Fetch story evaluations for the reader
    story_evals = StoryEval.objects.filter(reader=reader).select_related('story')

    # Serialize the data manually
    data = [
        {
            "id": str(eval.id),
            "story": {
                "id": str(eval.story.id),
                "title": eval.story.title,
                "author": eval.story.author,
                "link": eval.story.link,
            },
            "dateStarted": eval.dateStarted.strftime("%Y-%m-%d") if eval.dateStarted else None,
            "dateFinished": eval.dateFinished.strftime("%Y-%m-%d") if eval.dateFinished else None,
            "dateAdded": eval.dateAdded.strftime("%Y-%m-%d") if eval.dateAdded else None,
            "rating": eval.rating,
            "status": eval.status,
        }
        for eval in story_evals
    ]

    return JsonResponse(data, safe=False)
