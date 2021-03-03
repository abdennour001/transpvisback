from django.db import models
from transpvisback.enums import StakeholderTypes, InformationElementTypes, StakeholderInformationRelationshipTypes   


class Application(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"


class Stakeholder(models.Model):
    name = models.CharField(max_length=255)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.application.name} > {self.name}"


class InformationElement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=255, choices=InformationElementTypes.list(), default="data"
    )
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=False, null=False)
    information_elements = models.ManyToManyField('self', related_name='related_information_elements', blank=True)

    class Meta:
        verbose_name_plural = "Information Elements"
    
    def __str__(self):
        return f"{self.application.name} > {self.name}"


class StakeholderInformationRelationship(models.Model):
    stakeholder = models.ForeignKey(
        Stakeholder, on_delete=models.CASCADE, related_name="relationships_as_stakeholder"
    )
    information_element = models.ForeignKey(
        InformationElement, on_delete=models.CASCADE, related_name="relationships_as_ie"
    )
    type = models.CharField(
        max_length=255, choices=StakeholderInformationRelationshipTypes.list(), default="obligation"
    )

    class Meta:
        verbose_name_plural = "Stakeholder-information relationships"
        unique_together = ['stakeholder', 'information_element', 'type']

    def __str__(self):
        return f"({self.stakeholder, self.information_element, self.type})"
