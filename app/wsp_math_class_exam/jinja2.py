from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.template.defaultfilters import default_if_none

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['default_if_none'] = default_if_none
    return env
