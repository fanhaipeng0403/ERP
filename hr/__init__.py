"""
工资

"""
default_app_config = 'hr.apps.MyAppConfig'
"""

# 定义APP在admin接口的显示名称
# 可通过设置AppConfig的verbose_name实现，首先需创建apps.py文件，定义如下：
# 
# from django.apps import AppConfig
# 
# class MyConfig(AppConfig):
#     name = 'your name'
#     verbose_name = 'your display name'
# 
# 然后可以项目配置文件的INSTALL_APPS项中，把your app改为your app.MyConfig，或者在你的app的init.py定义default_app_config = ‘your app.MyConfig
"""
