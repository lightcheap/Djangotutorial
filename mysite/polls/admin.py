from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    モデルの admin のオプションを変更したいときには、
    モデルごとに admin クラスを作成して、 
    admin.site.register() の 2 番目の引数に渡すと いうパターン
    """
    list_display = ('question_text','pub_date','was_published_recently')
    fieldsets =[
        (None,             {'fields':['question_text']}),
        ('データインフォ',{'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
