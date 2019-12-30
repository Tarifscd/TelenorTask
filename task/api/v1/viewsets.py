import os
from django.http import Http404
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
import datetime
from rest_framework import permissions
from task.models import Keyvalue
from task.serializers import KeyvalueSerializer

from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

qrset = []
scheduler = BackgroundScheduler()
scheduler.start()
i = 0

def ttl_for_deleting_data():
    global qrset
    remove_users = []
    for record in qrset:
        remove_users.append(record.id)
        record.delete()

    qrset = qrset.exclude(id__in=remove_users)
    scheduler.remove_job('del')

def dlt():
    print('blahhhhhhhh')

scheduler.add_job(dlt, 'interval', id='del', seconds=2)





class KeyvalueViewSet(viewsets.ModelViewSet):
    queryset = Keyvalue.objects.all()
    serializer_class = KeyvalueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        key = self.request.GET.get('key')
        key_list = self.request.GET.get('keys')
        qs = super().get_queryset()
        if key:
            qs = qs.filter(key=key)

        filters = {}
        if key_list:
            filters['key__in'] = key_list.split(',')
            qs = qs.filter(**filters)

        global qrset
        qrset = qs

        if scheduler.get_jobs():
            scheduler.remove_job('del')
        scheduler.add_job(ttl_for_deleting_data, 'interval', id='del', minutes=5)

        return qs.order_by('id')

    def perform_update(self, serializer):
        qs = super().get_queryset()
        qs = qs.filter(id=serializer.instance.id)

        global qrset
        qrset = qs

        if scheduler.get_jobs():
            scheduler.remove_job('del')
        scheduler.add_job(ttl_for_deleting_data, 'interval', id='del', minutes=5)

        serializer.save()