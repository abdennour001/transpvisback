from rest_framework import serializers
from transparency.models import (
    Stakeholder,
    Application,
    InformationElement,
    StakeholderInformationRelationship,
    InformationElementAssociation,
)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = "__all__"


class InformationElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationElement
        fields = "__all__"


class StakeholderInformationRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakeholderInformationRelationship
        fields = "__all__"


class InformationElementAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationElementAssociation
        fields = "__all__"
