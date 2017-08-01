from django.contrib import admin
from .models import *

# Register your models here.

class VideoPageAdmin(admin.ModelAdmin):
	list_display = ('page_id', 'page_title', 'video_url')

class LyricsAdmin(admin.ModelAdmin):
	list_display = ('videoPage', 'start_time', 'end_time', 'content')

admin.site.register(VideoPage, VideoPageAdmin)
admin.site.register(Lyrics, LyricsAdmin)

