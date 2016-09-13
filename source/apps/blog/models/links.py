#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""

from django.db import models


class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    description = models.CharField(max_length=200, verbose_name=u'友情链接描述')
    callback_url = models.URLField(verbose_name=u'url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    index = models.IntegerField(default=999, verbose_name=u'排列顺序(从小到大)')

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


