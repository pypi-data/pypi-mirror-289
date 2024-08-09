"""
Created on 2024/8/9 上午11:46
@author:刘飞
@description:
"""
from django.utils.translation import gettext_lazy as _

celery_menu_list = [
    {
        'name': _('异步结果查看'),
        'models': [
            {
                'name': _('Task Result'),
                'url': 'django_celery_results/taskresult/'
            },
        ]
    }
]
