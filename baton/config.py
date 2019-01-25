# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.html import mark_safe
from django.utils.translation import ugettext as _

default_config = {
    'SITE_TITLE': 'Aplans',
    'SITE_HEADER': '<img style="width: 99px; height: 46px;" src="%sbaton/img/helsinki-logo-white.svg" />' % settings.STATIC_URL,
    'INDEX_TITLE': _('Site administration'),
    'SUPPORT_HREF': 'https://github.com/city-of-helsinki/aplans',
    'COPYRIGHT': 'City of Helsinki', # noqa
    'POWERED_BY': 'Hiilineutraali Helsinki',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
}


def get_config(key):
    safe = ['SITE_HEADER', 'COPYRIGHT', 'POWERED_BY', ]
    user_settings = getattr(settings, 'BATON', None)

    if user_settings is None:
        value = default_config.get(key, None)
    else:
        value = user_settings.get(key, default_config.get(key, None))

    if key in safe:
        return mark_safe(value)

    return value
 