# -*- coding: utf-8 -*-
from django.http.response import HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("/admin")
