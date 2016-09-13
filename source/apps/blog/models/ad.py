#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""

from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'广告标题')
    description = models.CharField(max_length=200,  verbose_name=u'广告描述')
    image_url = models.ImageField(upload_to=u'ad/%Y/%m', verbose_name=u'图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name=u'回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    index = models.IntegerField(default=999, verbose_name=u'排列顺序(从小到大)')

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title
