from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addons/(?P<guid>[^/]+)/versions/(?P<version>[^/]+)/$',
        views.VersionView.as_view(),
        name='signing.version'),
]
