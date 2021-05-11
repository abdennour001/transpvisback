from django.shortcuts import render
from transpvisback.views import (
    ListView,
    RetrieveView,
    CreateView,
    UpdateView,
    DestroyView,
)
from transparency.models import (
    Stakeholder,
    Application,
    InformationElement,
    StakeholderInformationRelationship,
    InformationElementAssociation,
)
from transparency.serializers import (
    StakeholderSerializer,
    ApplicationSerializer,
    InformationElementSerializer,
    StakeholderInformationRelationshipSerializer,
    InformationElementAssociationSerializer,
)
from rest_framework import permissions


class ApplicationDetail(RetrieveView, UpdateView, DestroyView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationList(ListView, CreateView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.AllowAny,)


class StakeholderDetail(RetrieveView, UpdateView, DestroyView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer


class StakeholderList(ListView, CreateView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "application",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]


class InformationElementDetail(RetrieveView, UpdateView, DestroyView):
    queryset = InformationElement.objects.all()
    serializer_class = InformationElementSerializer


class InformationElementList(ListView, CreateView):
    queryset = InformationElement.objects.all()
    serializer_class = InformationElementSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "application",
        "type",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]


class StakeholderInformationRelationshipDetail(RetrieveView, UpdateView, DestroyView):
    queryset = StakeholderInformationRelationship.objects.all()
    serializer_class = StakeholderInformationRelationshipSerializer


class StakeholderInformationRelationshipList(ListView, CreateView):
    queryset = StakeholderInformationRelationship.objects.all()
    serializer_class = StakeholderInformationRelationshipSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = [
        "stakeholder",
        "information_element",
        "stakeholder__application",
    ]


class InformationElementAssociationDetail(RetrieveView, UpdateView, DestroyView):
    queryset = InformationElementAssociation.objects.all()
    serializer_class = InformationElementAssociationSerializer


class InformationElementAssociationList(ListView, CreateView):
    queryset = InformationElementAssociation.objects.all()
    serializer_class = InformationElementAssociationSerializer
