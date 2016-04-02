from django.contrib import admin
from .models import Question, Choice, Nform, Post

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Nform)
admin.site.register(Post)
