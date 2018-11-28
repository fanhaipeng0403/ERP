# -*- coding: utf-8 -*-
"""
WSGI config for mis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.contrib import admin

admin.site.site_header = 'ERP'
admin.site.site_title = 'ERP'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mis.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
