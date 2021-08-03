from django.db import models
from apps.drinks.models import Product

# Create your models here.
class Order(models.Model):
    # 订单模型
    status_choices = (
        (0, '已下单'),
        (1, '制作中'),
        (2, '可取茶'),
    )
    total_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="订单总价", default=0)
    order_number = models.CharField(max_length=64, verbose_name="订单号")
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    order_desc = models.TextField(max_length=500, verbose_name="订单描述")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    # user = models.ForeignKey(User, related_name='user_orders', on_delete=models.DO_NOTHING, verbose_name="下单用户")
    # shop = models.ForeignKey()
    # product = models.ForeignKey()

class OrderDetail(models.Model):
    # 订单详情
    order = models.ForeignKey(Order, related_name='order_courses', on_delete=models.CASCADE, verbose_name="订单")
    # product = models.ForeignKey(Product, related_name=)
