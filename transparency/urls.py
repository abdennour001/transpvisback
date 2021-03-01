from django.urls import path
from transparency.views import (
    StakeholderDetail,
    StakeholderList,
    ApplicationDetail,
    ApplicationList,
    InformationElementDetail,
    InformationElementList,
    StakeholderInformationRelationshipDetail,
    StakeholderInformationRelationshipList,
)

urlpatterns = [
    path("applications/<int:pk>/", ApplicationDetail.as_view()),
    path("applications/", ApplicationList.as_view()),
    path("stakeholders/<int:pk>/", StakeholderDetail.as_view()),
    path("stakeholders/", StakeholderList.as_view()),
    path("information-elements/<int:pk>/", InformationElementDetail.as_view()),
    path("information-elements/", InformationElementList.as_view()),
    path("stakeholder-information-relationships/<int:pk>/", StakeholderInformationRelationshipDetail.as_view()),
    path("stakeholder-information-relationships/", StakeholderInformationRelationshipList.as_view()),
]
