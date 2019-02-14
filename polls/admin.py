from django.contrib import admin

from .models import Choice, Question

# Register your models here.

# had first tried admin.StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# sample modification below adds fieldsets
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['question_text']}),
        ('Date information',   {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# removed after making Choice inline - adding choices on the question page
#admin.site.register(Choice)
