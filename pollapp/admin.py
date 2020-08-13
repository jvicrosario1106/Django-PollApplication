from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoicesTab(admin.TabularInline):
    model = Choice
    extra = 0
    

class QuestionAdmin(admin.ModelAdmin):
    models = Question
    inlines = [ChoicesTab]


admin.site.register(Question,QuestionAdmin)
