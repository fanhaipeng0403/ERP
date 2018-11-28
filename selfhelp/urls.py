# -*- coding: utf-8 -*-
import selfhelp.views
from django.conf.urls import url

urlpatterns = [
    url(r"(?P<model>\w+)/(?P<object_id>\d+)/pay", selfhelp.views.pay_action),
]
