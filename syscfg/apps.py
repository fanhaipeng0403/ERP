# -*- coding: utf-8 -*-


from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _


class SysConfig(AppConfig):
    name = 'syscfg'
    verbose_name = _('SysConfig')
