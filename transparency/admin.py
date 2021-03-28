from django.contrib import admin

from django.contrib import admin
from transparency.models import (
    Application,
    Stakeholder,
    InformationElement,
    StakeholderInformationRelationship,
    InformationElementAssociation,
)


admin.site.register(
    [
        Stakeholder,
        StakeholderInformationRelationship,
        Application,
        InformationElementAssociation,
    ]
)


class InformationElementAssociationInline(admin.TabularInline):
    model = InformationElementAssociation
    fk_name = "source"
    autocomplete_fields = ("target",)
    extra = 0
    min_num = 0


@admin.register(InformationElement)
class InformationElementAdmin(admin.ModelAdmin):
    search_fields = (
        "application__name",
        "name",
    )
    inlines = (InformationElementAssociationInline,)
