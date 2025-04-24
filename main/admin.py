from django.contrib import admin

from main.models import Card, IFile


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'right_answer',
        'answer1',
        'answer2',
        'answer3'
    )
    search_fields = ('question',)


@admin.register(IFile)
class IFileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'value'
    )
