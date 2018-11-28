# -*- coding: utf-8 -*-
from django.conf.urls import include, url, static
from django.contrib import admin

import mis.views
import workflow.views
from mis import settings

urlpatterns = [
    url(r'^$', mis.views.home),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", workflow.views.start),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)", workflow.views.approve),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", workflow.views.restart),
    # 尾部无/
    # url(r'^admin/', admin.site.urls),
    url(r'^admin',  admin.site.urls),
    url(r'^admin/invent/', include('invent.urls')),
    url(r'^admin/basedata/', include('basedata.urls')),
    url(r'^admin/selfhelp/', include('selfhelp.urls')),
]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
