from django.urls import path
from authentication.views import (
    UserDetail,
    UserList,
    LoginView,
    Register,
)

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("users/", UserList.as_view()),
    path("register/", Register.as_view()),
]