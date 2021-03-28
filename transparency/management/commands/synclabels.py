from django.core.management.base import BaseCommand
from transparency.models import Application, Stakeholder, InformationElement
from transpvisback.enums import InformationElementTypes

class Command(BaseCommand):
    help = "Sync stakeholders and information elements labels."

    def handle(self, *args, **options):
        for application in Application.objects.all():
            s_count, d_count, r_count, p_count = 1, 1, 1, 1
            for stakeholder in application.stakeholders.all():
                stakeholder.label = "S{:0>3d}".format(s_count)
                stakeholder.save()
                s_count += 1
            for data in application.information_elements.filter(type=InformationElementTypes.DATA):
                data.label = "D{:0>3d}".format(d_count)
                data.save()
                d_count += 1
            for process in application.information_elements.filter(type=InformationElementTypes.PROCESS):
                process.label = "R{:0>3d}".format(r_count)
                process.save()
                r_count += 1
            for policy in application.information_elements.filter(type=InformationElementTypes.POLICY):
                policy.label = "P{:0>3d}".format(p_count)
                policy.save()
                p_count += 1