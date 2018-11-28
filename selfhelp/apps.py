



from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = 'selfhelp'
    verbose_name = _("self help")
