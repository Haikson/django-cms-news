from django.contrib import admin
from models import News
from django import forms

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'published')

    class Media:
        js = (
            #'/media/js/ckeditor/ckeditor.js',
            #'/media/js/ckeditor_filer.js',
            #'/media/filebrowser/js/fb_ckeditor.js',
            '/static/filebrowser/js/FB_CKEditor.js',
        )
        #css = { 'all': ('/media/js/ckeditor/css/ckeditor.css',),}

admin.site.register(News, NewsAdmin)