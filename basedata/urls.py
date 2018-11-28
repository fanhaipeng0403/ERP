# -*- coding: utf-8 -*-
from django.conf.urls import url

import basedata.views

urlpatterns = [
    url(r"dataimport/(?P<object_id>\d+)/action", basedata.views.action_import),
]
