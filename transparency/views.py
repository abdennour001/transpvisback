from django.shortcuts import render
from transpvisback.views import ListView, RetrieveView
from transparency.models import (
    Stakeholder,
    Application,
    InformationElement,
    StakeholderInformationRelationship,
)
from transparency.serializers import (
    StakeholderSerializer,
    ApplicationSerializer,
    InformationElementSerializer,
    StakeholderInformationRelationshipSerializer,
)
from rest_framework import permissions


class ApplicationDetail(RetrieveView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationList(ListView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.AllowAny,)


class StakeholderDetail(RetrieveView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer


class StakeholderList(ListView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "application",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]


class InformationElementDetail(RetrieveView):
    queryset = InformationElement.objects.all()
    serializer_class = InformationElementSerializer


class InformationElementList(ListView):
    queryset = InformationElement.objects.all()
    serializer_class = InformationElementSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "application",
        "type",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]


class StakeholderInformationRelationshipDetail(RetrieveView):
    queryset = StakeholderInformationRelationship.objects.all()
    serializer_class = StakeholderInformationRelationshipSerializer


class StakeholderInformationRelationshipList(ListView):
    queryset = StakeholderInformationRelationship.objects.all()
    serializer_class = StakeholderInformationRelationshipSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "stakeholder",
        "information_element",
        "stakeholder__application",
    ]
