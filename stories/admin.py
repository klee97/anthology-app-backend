from django.contrib import admin
from .models import Reader, Story, StoryEval

admin.site.register(Story)
admin.site.register(StoryEval)
admin.site.register(Reader)