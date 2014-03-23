django-cms-news
===============

The 'News' app for django &amp;&amp; django-cms

Installation
------------

```sh
pip install -e git@github.com:Haikson/django-cms-news.git
```

Requirements
------------

* [djangocms_text_ckeditor link](https://github.com/divio/djangocms-text-ckeditor)
* [pytils link](https://github.com/j2a/pytils)

Usage
-----

Add ```news, django_text_ckeditor, pytils``` to ```INSTALLED_APPS```

```python
INSTALLED_APPS = (
    # ..........
    'django_text_ckeditor',
    'pytils',
    'news',
    # ..........
)
```
