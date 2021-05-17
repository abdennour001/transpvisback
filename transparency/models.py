from django.db import models
from transpvisback.enums import (
    StakeholderTypes,
    InformationElementTypes,
    StakeholderInformationRelationshipTypes,
)
from django.core.validators import MaxValueValidator, MinValueValidator


class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    transparency_note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        "authentication.user",
        related_name="applications",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"


class Stakeholder(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    application = models.ForeignKey(
        Application,
        related_name="stakeholders",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    weight = models.IntegerField(
        default=0, validators=[MaxValueValidator(1), MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.application.name} > {self.name}"


class InformationElement(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=255, choices=InformationElementTypes.list(), default="data"
    )
    application = models.ForeignKey(
        Application,
        related_name="information_elements",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    information_elements = models.ManyToManyField(
        "self",
        related_name="related_information_elements",
        through="transparency.InformationElementAssociation",
        blank=True,
        symmetrical=False,
    )
    weight = models.IntegerField(
        default=0, validators=[MaxValueValidator(1), MinValueValidator(0)]
    )

    class Meta:
        verbose_name_plural = "Information Elements"

    def __str__(self):
        return f"{self.application.name} > {self.name}"


class StakeholderInformationRelationship(models.Model):
    stakeholder = models.ForeignKey(
        Stakeholder,
        on_delete=models.CASCADE,
        related_name="relationships_as_stakeholder",
    )
    information_element = models.ForeignKey(
        InformationElement, on_delete=models.CASCADE, related_name="relationships_as_ie"
    )
    type = models.CharField(
        max_length=255,
        choices=StakeholderInformationRelationshipTypes.list(),
        default="obligation",
    )

    class Meta:
        verbose_name_plural = "Stakeholder-information relationships"
        unique_together = ["stakeholder", "information_element", "type"]

    def __str__(self):
        return f"{self.stakeholder}, {self.information_element}, {self.type}"


class InformationElementAssociation(models.Model):
    source = models.ForeignKey(
        InformationElement, on_delete=models.CASCADE, related_name="source_associations"
    )
    target = models.ForeignKey(
        InformationElement, on_delete=models.CASCADE, related_name="target_associations"
    )

    def __str__(self):
        return f"{self.source.name} > {self.target.name}"

    class Meta:
        unique_together = ["source", "target"]
