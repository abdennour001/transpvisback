from django.urls import path
from transparency.views import (
    StakeholderDetail,
    StakeholderList,
)

urlpatterns = [
    path("stakeholders/<int:pk>/", StakeholderDetail.as_view()),
    path("stakeholders/", StakeholderList.as_view()),
]
