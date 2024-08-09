"""
Created on 2024/8/9 下午2:46
@author:刘飞
@description:
"""
from django.urls import re_path
from .api.celery_test import CeleryTasksTest

urlpatterns = [
    re_path(r"^add/?$", CeleryTasksTest.as_view(), name="add"),
]
