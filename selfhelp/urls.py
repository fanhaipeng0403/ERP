# -*- coding: utf-8 -*-
from django.conf.urls import url

import selfhelp.views

urlpatterns = [
    url(r"(?P<model>\w+)/(?P<object_id>\d+)/pay", selfhelp.views.pay_action),
]
