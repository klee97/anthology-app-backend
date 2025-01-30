from django.core.serializers import serialize
from django.http import JsonResponse

from .models import Story
# Create your views here.

def detail(request, id):
  story = Story.objects.get(id=id)
  story_json = serialize('json', [story])
  return JsonResponse(story_json, safe=False)

def all_stories(request):
  stories = Story.objects.values('id', 'title', 'author')
  return JsonResponse(list(stories), safe=False)
