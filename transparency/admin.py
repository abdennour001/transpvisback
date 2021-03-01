from django.contrib import admin

from django.contrib import admin
from transparency.models import Application, Stakeholder, InformationElement, StakeholderInformationRelationship


admin.site.register([Stakeholder, InformationElement, StakeholderInformationRelationship, Application])