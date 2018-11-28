# -*- coding: utf-8 -*-


from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrganConfig(AppConfig):
    name = 'organ'
    verbose_name = _('organization')
