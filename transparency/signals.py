from django.db.models.signals import post_save
from transparency.models import Application, Stakeholder, InformationElement
from transpvisback.enums import InformationElementTypes


def stakeholder_post_save(sender, instance, created, **kwargs):
    if created:
        instance.label = "S{:0>3d}".format(
            Stakeholder.objects.filter(application=instance.application).count()
        )
        instance.save()


def information_element_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.type == "data":
            instance.label = "D{:0>3d}".format(
                InformationElement.objects.filter(
                    application=instance.application, type=InformationElementTypes.DATA
                ).count()
            )
            print(instance.label)
            instance.save()
        elif instance.type == "process":
            instance.label = "R{:0>3d}".format(
                InformationElement.objects.filter(
                    application=instance.application,
                    type=InformationElementTypes.PROCESS,
                ).count()
            )
            instance.save()
        elif instance.type == "policy":
            instance.label = "P{:0>3d}".format(
                InformationElement.objects.filter(
                    application=instance.application,
                    type=InformationElementTypes.POLICY,
                ).count()
            )
            instance.save()


post_save.connect(
    information_element_post_save, sender=InformationElement, dispatch_uid="ie-signal"
)
post_save.connect(
    stakeholder_post_save, sender=Stakeholder, dispatch_uid="stakeholder-signal"
)
