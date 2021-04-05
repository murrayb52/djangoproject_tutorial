from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# To customise the admin form, create a model admin class then pass it as the second argument
# to admin.site.register().
# This particular change above makes the “Publication date” come before the “Question” field:
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # This adds a filter sidebar option to the admin page to filter out questions by pub_date
    list_filter = ['pub_date']
    # Search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)