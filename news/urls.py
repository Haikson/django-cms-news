from django.conf.urls import url, patterns

urlpatterns = patterns('news.views',
    url(r'^$', 'news', name='news_news'),
    url(r'^(?P<slug>[\w-]+)/$', 'the_news', name='news_the_news'),
)