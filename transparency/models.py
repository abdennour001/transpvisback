from django.db import models
from transpvisback.enums import StakeholderTypes, InformationElementTypes, StakeholderInformationRelationshipTypes   


class Stakeholder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class InformationElement(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255, choices=InformationElementTypes.list(), default="data"
    )

    class Meta:
        verbose_name_plural = "Information Elements"
    
    def __str__(self):
        return self.name


class StakeholderInformationRelationship(models.Model):
    stakeholder = models.ForeignKey(
        Stakeholder, on_delete=models.CASCADE, related_name="relationships"
    )
    information_element = models.ForeignKey(
        Stakeholder, on_delete=models.CASCADE, related_name="relationships"
    )
    type = models.CharField(
        max_length=255, choices=StakeholderInformationRelationshipTypes.list(), default="obligation"
    )

    class Meta:
        verbose_name_plural = "Stakeholder-information relationships"