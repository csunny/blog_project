#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""
from django.contrib import admin
from blog.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _


class BlogUserAdmin(UserAdmin):
    filesets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('email', 'qq', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': {'last_login', 'date_joined'}}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, BlogUserAdmin)