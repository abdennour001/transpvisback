from django.shortcuts import render
from transpvisback.views import ListView, RetrieveView
from transparency.models import Stakeholder
from transparency.serializers import StakeholderSerializer
from rest_framework import permissions


class StakeholderDetail(RetrieveView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer


class StakeholderList(ListView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer
    permission_classes = (permissions.AllowAny,)