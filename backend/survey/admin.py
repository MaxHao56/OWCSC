from django.contrib import admin
from .models import Survey, Questions, Responses


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Responses)
class ResponsesAdmin(admin.ModelAdmin):
    pass
# Register your models here.
