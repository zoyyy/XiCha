from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class UserExtension(models.Model):
    """
    用户
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    nickname = models.CharField(max_length=256)
    mobile = models.CharField(null=True, blank=False, max_length=11)
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female")
    birthday = models.DateField(null=True, blank=True)
    wallet = models.DecimalField(max_digits=6, decimal_places=2, default=100)

# 接受保存模型的信号处理方法，只要是User调用了save方法，那么就会创建一个UserExtension和User进行绑定。
@receiver(post_save, sender=User)
def create_user_extension(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()