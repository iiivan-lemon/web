from django.contrib import admin

from app import models

admin.site.register(models.Question)
admin.site.register(models.Tags)
admin.site.register(models.Answer)