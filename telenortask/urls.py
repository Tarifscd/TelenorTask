from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from task import views
# from task.api.v1.viewsets import scheduler

urlpatterns = [
    url(r'^task/', include('task.task_urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('task.urls')),
]


