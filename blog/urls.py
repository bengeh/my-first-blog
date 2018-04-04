from django.conf.urls import url
from . import views
from django.contrib.auth import views as djview

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]

# urlpatterns_accounts = [
    # url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),

# ]
urlpatterns_accounts = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^registration/login/$', djview.login, name='login'),
    url(r'^registration/logout/$', djview.logout, name='logout'),
]


urlpatterns.extend(urlpatterns_accounts)