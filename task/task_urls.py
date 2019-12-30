from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^api/', include('task.api.api_urls')),
]