from django.contrib import admin
from api.models import Link, ValidCode, UsedCode


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'code')


@admin.register(ValidCode)
class ValidCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(UsedCode)
class UsedCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)
