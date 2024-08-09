"""
Created on 2024/8/9 下午2:44
@author:刘飞
@description:
异步测试
"""
import time
from celery import shared_task


@shared_task
def add(x, y):
    print('进入add方法')
    time.sleep(5)
    print('离开add方法')
    return x + y


@shared_task
def mul(x, y):
    return x * y
