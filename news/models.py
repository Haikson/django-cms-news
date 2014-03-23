from django.db import models
from django.utils.translation import ugettext_lazy as _
from pytils.translit import slugify
from djangocms_text_ckeditor.fields import HTMLField

class NewsManager(models.Manager):
    def last(self, count=None):
        if count is None:
            count = 10
        return self.all().filter(published=True).order_by('-created')[0:count]

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    slug = models.CharField(max_length=60, verbose_name=_('Slug'), null=True, blank=True)
    intro = models.TextField(verbose_name=_('Intro'))
    content = HTMLField(verbose_name=_('Content'))
    created = models.DateTimeField(verbose_name=_('Created time'))
    published = models.BooleanField()

    objects = NewsManager()

    def clean(self):
        if not self.slug:
            slug = slugify(self.title)
        else:
            slug = slugify(self.slug)

        self.slug = slug

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = _('The News')
        verbose_name_plural = _('News')

try:
    from cms.models import CMSPlugin
    class NewsListPlugin(CMSPlugin):
        TEMPLATE_CHOICES = (
            ('aside.html', _('Aside template')),
            ('inner_list.html', _('News list template')),
        )
        count = models.IntegerField(verbose_name=_('Count of news'))
        template = models.CharField(max_length=255, verbose_name=_('Template'), choices=TEMPLATE_CHOICES)
except:
    pass

    def __unicode__(self):
        return '%s' % self.count
