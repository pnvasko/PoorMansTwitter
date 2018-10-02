from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .view import TwittersView, twitters_add

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls, name='admin'),
    url(r'^api/v1/twitter$', twitters_add, name='twitters_add'),
    url(r'^api/v1/twitters[/]?$', TwittersView.as_view(), name='twitters_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

admin.site.site_header = 'PoorMansTwitter 0.0.1'
admin.site.site_title = 'PoorMansTwitter 0.0.1'
