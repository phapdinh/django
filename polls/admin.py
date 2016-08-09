from django.contrib import admin

from .models import Question

#Makes admin page show more details for entry
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date']

admin.site.register(Question, QuestionAdmin)
