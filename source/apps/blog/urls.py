from django.conf.urls import url

from blog.views.article import index, archive, article, comment_post, do_logout, do_login, do_reg, category, tag

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^article/$', article, name='article'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^category/$', category, name='category'),
    url(r'^tag/$', tag, name='tag'),
]
