# -*- coding: utf-8 -*-




from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = 'hr'
    verbose_name = _("human resource")
