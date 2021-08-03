from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.utils import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


class Users:
    @staticmethod
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @staticmethod
    def login_user(request):
        print(request.body)
        print(request.method)
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            if username is not None and password is not None:
                islogin = authenticate(request, username=username, password=password)
                if islogin:
                    login(request, islogin)
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": username
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "登录失败, 请检查用户名或者密码是否输入正确."
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            JsonResponse({
                "status": 3,
                "message": "参数错误"
            })

    @staticmethod
    def logout_user(request):
        logout(request)
        return JsonResponse({
            "status": 0
        })

    @staticmethod
    def register(request):
        if request.method == "POST":
            data = json.loads(request.body)

            if request.GET.get("select") is not None:
                select_username = data.get("select_username")
                print(select_username)
                try:
                    User.objects.get(username=select_username)
                    return JsonResponse({
                        "status": 0,
                        "is_indb": 1
                    })
                except:
                    return JsonResponse({
                        'status': 0,
                        "is_indb": 0
                    })
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")
            mobile = data.get("mobile")
            print(username)
            print(password)
            print(email)
            if username is not None and password is not None and email is not None:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()

                    login_user = authenticate(request, username=username, password=password)
                    if login_user:
                        login(request, login_user)
                        return JsonResponse({
                            "status": 0,
                            "message": "Register and Login Success"
                        })

                except:
                    return JsonResponse({
                        "status": 2,
                        "message": "注册失败, 该用户名已经存在."
                    })
            else:
                print('create fail')
        else:
            return JsonResponse({
                "status": 1,
                "message": "error method"
            })
