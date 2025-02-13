from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Story
from .models import StoryEval, Reader
# Create your views here.

def detail(request, id):
  story = Story.objects.get(id=id)
  story_json = serialize('json', [story])
  return JsonResponse(story_json, safe=False)

def all_stories(request):
  stories = Story.objects.values('id', 'title', 'author')
  return JsonResponse(list(stories), safe=False)


def reader_story_evals(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch the user by ID
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
            "rating": eval.rating,
            "status": eval.status,
        }
        for eval in story_evals
    ]

    return JsonResponse(data, safe=False)