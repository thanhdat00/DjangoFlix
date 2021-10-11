from django.contrib import admin
from django.db.models.base import Model

# Register your models here.
from .models import VideoAllProxy, VideoPublishedProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id', 'is_published']
    class Meta:
        model = VideoAllProxy

admin.site.register(VideoAllProxy, VideoAllAdmin)

class VideoPublishedAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoAllProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoPublishedAdmin)