#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name=u'用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=u'手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name=u'个人网页地址')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username
