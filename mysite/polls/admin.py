from django.contrib import admin

# Register your models here.from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.


admin.site.register(Question)
admin.site.register(Choice)
