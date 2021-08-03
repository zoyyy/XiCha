"""xicha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.users import views
from apps.drinks import views as drink
# from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

urlpatterns = [
    path('admin/', admin.site.urls),
    # # 验证用户并生成token
    # path('token/', ObtainJSONWebToken.as_view(), name="token_obtain_pair"),
    # # 刷新token
    # path('token/refresh/', RefreshJSONWebToken.as_view(), name='token_refresh'),
    path('login/', views.Users.login_user),  # 登录
    path('register/', views.Users.register),  # 注册
    path('drinks/', drink.CategoryView.as_view()),  # 订单页面
]
