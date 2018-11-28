# -*- coding: utf-8 -*-
import basedata.views
from django.conf.urls import url

urlpatterns = [
    url(r"dataimport/(?P<object_id>\d+)/action", basedata.views.action_import),
]
