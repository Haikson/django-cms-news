from django.contrib import admin
from models import News
from django import forms
from django.conf import settings
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'published')

    class Media:
        if 'filebrowser' in settings.INSTALLED_APP:
            js = (
                '/static/js/ckeditor_fb.js',
                '/static/filebrowser/js/FB_CKEditor.js',
            )
        else:
            pass
        
admin.site.register(News, NewsAdmin)
