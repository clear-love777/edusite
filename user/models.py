from django.db import models


# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=16, verbose_name="账号", unique=True)
    username = models.CharField(max_length=11, verbose_name="昵称")
    password = models.CharField(max_length=50, verbose_name="密码")
    head_img = models.ImageField(upload_to='static/image', verbose_name="头像", default='')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    isActive = models.BooleanField(verbose_name="活跃状态",default=True)
    # 三种角色:student teacher admin 默认student
    user_role = models.CharField(max_length=11,verbose_name="角色",default="student")

    email = models.EmailField(verbose_name="邮箱",default="")
    phone = models.CharField(verbose_name="联系方式",max_length=16,default='')