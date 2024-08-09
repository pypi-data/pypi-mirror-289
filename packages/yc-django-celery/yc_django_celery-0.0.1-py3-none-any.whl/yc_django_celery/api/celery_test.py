"""
Created on 2024/8/9 下午2:52
@author:刘飞
@description:
功能测试
"""
from rest_framework.views import APIView
from yc_django_utils.json_response import DetailResponse
from ..tasks import add, mul


class CeleryTasksTest(APIView):
    """
    get:异步测试
    """

    def get(self, request):
        res = add.delay(1, 3)
        data = {
            'task_id': res.task_id
        }
        return DetailResponse(data)
