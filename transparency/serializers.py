from rest_framework import serializers
from transparency.models import Stakeholder, Application, InformationElement, StakeholderInformationRelationship


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

