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
from rest_framework import status
from rest_framework.response import Response


class ApplicationDetail(RetrieveView, UpdateView, DestroyView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(
            user=self.request.user,
        )


class ApplicationList(ListView, CreateView):
    serializer_class = ApplicationSerializer
    filterset_fields = [
        "user",
    ]

    def get_queryset(self):
        return Application.objects.filter(
            user=self.request.user,
        )


class StakeholderDetail(RetrieveView, UpdateView, DestroyView):
    serializer_class = StakeholderSerializer

    def get_queryset(self):
        return Stakeholder.objects.filter(
            application__user=self.request.user,
        )


class StakeholderList(ListView, CreateView):
    serializer_class = StakeholderSerializer
    filterset_fields = [
        "application",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]

    def get_queryset(self):
        return Stakeholder.objects.filter(
            application__user=self.request.user,
        )


class InformationElementDetail(RetrieveView, UpdateView, DestroyView):
    serializer_class = InformationElementSerializer

    def get_queryset(self):
        return InformationElement.objects.filter(
            application__user=self.request.user,
        )


class InformationElementList(ListView, CreateView):
    queryset = InformationElement.objects.all()
    serializer_class = InformationElementSerializer
    filterset_fields = [
        "application",
        "type",
    ]
    ordering_fields = ["application", "label"]
    ordering = ["application", "label"]

    def get_queryset(self):
        return InformationElement.objects.filter(
            application__user=self.request.user,
        )


class StakeholderInformationRelationshipDetail(RetrieveView, UpdateView, DestroyView):
    serializer_class = StakeholderInformationRelationshipSerializer

    def get_queryset(self):
        return StakeholderInformationRelationship.objects.filter(
            stakeholder__application__user=self.request.user,
        )


class StakeholderInformationRelationshipList(ListView, CreateView):
    serializer_class = StakeholderInformationRelationshipSerializer
    filterset_fields = [
        "stakeholder",
        "information_element",
        "stakeholder__application",
    ]

    def get_queryset(self):
        return StakeholderInformationRelationship.objects.filter(
            stakeholder__application__user=self.request.user,
        )


class InformationElementAssociationDetail(RetrieveView, UpdateView):
    serializer_class = InformationElementAssociationSerializer

    def get_queryset(self):
        return InformationElementAssociation.objects.filter(
            source__application__user=self.request.user,
        )


class InformationElementAssociationList(ListView, CreateView, DestroyView):
    serializer_class = InformationElementAssociationSerializer

    def get_queryset(self):
        return InformationElementAssociation.objects.filter(
            source__application__user=self.request.user,
        )

    def delete(self, request, *args, **kwargs):
        try:
            source = request.data["source"]
            target = request.data["target"]
            association = InformationElementAssociation.objects.get(
                source=source, target=target
            )
            association.delete()
            return Response(status.HTTP_200_OK)
        except:
            return Response(
                {"status": "association not found"}, status=status.HTTP_404_NOT_FOUND
            )
