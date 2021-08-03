from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.utils import json
from django.views import View
from .models import *

# Create your views here.

class CategoryView(View):
    # 获取店铺名称
    # 获取目录列表
    def get_cate(self, request):
        Categories = Category.objects.filter(is_delete=False)
        data = {
            "code": 0,
            "msg": "success",
            "categories": Categories
        }
        return  JsonResponse(data)

    # 获取饮品介绍
    def get_drink(self, request):
        Drink = Product.objects.filter(is_delete=False)
        data = {
            "code": 0,
            "msg": "success",
            "product": Drink
        }
        return  JsonResponse(data)
