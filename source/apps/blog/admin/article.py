#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""
from blog.models import Article, Tag, Category, Comment
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)


