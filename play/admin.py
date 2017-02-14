from django.contrib import admin

# Register your models here.

from .models import *


class SongDetailsFormAdmin(admin.StackedInline):
    model = SongDetailsForm
    extra = 1


class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'tabs_and_chords', 'tags', 'genre']})
    ]
    inlines = [SongDetailsFormAdmin]


admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
