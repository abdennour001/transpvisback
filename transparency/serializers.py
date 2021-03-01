from rest_framework import serializers
from transparency.models import Stakeholder


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = "__all__"
