from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mem$', views.mem, name='mem'),
    url(r'^addmem/$', views.addmem, name='addmem'),
    url(r'^mem/get/(?P<id>\d+)/$', views.getmem, name='getmem'),
    url(r'^mem/delmem/(?P<id>\d+)/$', views.delmem),
    url(r'^memuser/(\d+)/page/(\d+)/$', views.memuser),
    url(r'^mem/addlike/(?P<id>\d+)/$', views.liking),
    url(r'^memsortdate/page/(\d+)/$', views.sort),
    url(r'^memsortlike/page/(\d+)/$', views.sortlike),
    url(r'^memsortlike/memuser/(?P<id>\d+)/page/(?P<page_number>\d+)/$', views.sortlike),
    url(r'^memsortdate/memuser/(?P<id>\d+)/page/(?P<page_number>\d+)/$', views.sort),
    url(r'^page/(\d+)/$', views.mem),
    url(r'^profile/(?P<id>\d+)/$', views.profile),
    url(r'^profile/(?P<id>\d+)/upd/$', views.profileupd),
    url(r'^$', views.mem, name='mem'),
]