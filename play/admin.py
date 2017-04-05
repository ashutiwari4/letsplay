from django.contrib import admin

# Register your models here.

from .models import *


class SongDetailsFormAdmin(admin.StackedInline):
    model = ImageDetailsForm
    extra = 1


class VideoLinkDetailsFormForAdmin(admin.StackedInline):
    model = VideoLinksForm
    extra = 1


class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'tabs', 'chords', 'tags', 'genre']})
    ]
    inlines = [SongDetailsFormAdmin, VideoLinkDetailsFormForAdmin]


admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
admin.site.register(LinkType)
