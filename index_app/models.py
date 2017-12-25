from django.db import models
from django.contrib import admin

# Create your models here.
class SystemInfo(models.Model):
    url = models.CharField(max_length=100, default='')
    # image = models.CharField(max_length=100, blank=True, default='')
    image = models.FileField(upload_to='icons')
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, blank=True, default='All')
    mark = models.IntegerField(unique=True)
    desc = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['-mark']
        # ordering = ['id']
        verbose_name = '系统信息'
        verbose_name_plural = '系统信息'

# class UserInfo(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name = '用户'
#         verbose_name_plural = '用户'
