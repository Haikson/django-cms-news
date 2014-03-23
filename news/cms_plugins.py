from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import NewsListPlugin as NewsListPluginModel, News
from django.utils.translation import ugettext_lazy as _

class NewsListPlugin(CMSPluginBase):
    model = NewsListPluginModel
    name = _('News List Plugin')
    render_template = 'news/list.html'

    def render(self, context, instance, placeholder):
        template = 'news/%s' % instance.template
        count = instance.count
        news = News.objects.last(count)
        context.update({'news': news, 'template': template})
        return context

plugin_pool.register_plugin(NewsListPlugin)
