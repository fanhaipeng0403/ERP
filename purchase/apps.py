



from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = 'purchase'
    verbose_name = _("purchase manage")
