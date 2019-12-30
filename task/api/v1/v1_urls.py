from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from task.api.v1 import viewsets
from task import views

router = DefaultRouter()
router.register('keyvalues', viewsets.KeyvalueViewSet)
# router.register('keyvalues', viewsets.KeyvalueList, 'keyvalues')

# urlpatterns = router.urls
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^keyvalues/', viewsets.KeyvalueList.as_view()),
]