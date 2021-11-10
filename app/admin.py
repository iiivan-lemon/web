from django.contrib import admin

from app import models

admin.site.register(models.Question)
admin.site.register(models.User)
admin.site.register(models.Author)
admin.site.register(models.Tags)
admin.site.register(models.Answer)
admin.site.register(models.AnswerLikes)
admin.site.register(models.QuestionLikes)