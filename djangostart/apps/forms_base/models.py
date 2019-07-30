from django.db import models
import json

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=18)
    password = models.CharField(verbose_name="密码",max_length=128)

    def __str__(self):
        return self.username

    def to_dict(self):
        return dict([(attr,getattr(self,attr)) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = verbose_name



