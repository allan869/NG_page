from django.conf.urls import url
from index_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^infos$', views.SystemInfoList.as_view()),
    url(r'^infos/(?P<pk>[0-9]+)$', views.SystemInfoDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)