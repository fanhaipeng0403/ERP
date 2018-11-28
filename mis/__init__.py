import pymysql

pymysql.install_as_MySQLdb()
from django.contrib import admin

admin.site.site_header = 'ERP'
admin.site.site_title = 'ERP'
