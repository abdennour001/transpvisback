from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import logout, authenticate, login
from authentication.serializers import UserSerializer, LoginSerializer
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from transpvisback.views import (
    ListView,
    RetrieveView,
    CreateView,
    UpdateView,
    DestroyView,
)
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.data["email"], password=serializer.data["password"]
        )
        if user:
            return Response(
                {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "token": user.auth_token.key,
                }
            )
        else:
            raise AuthenticationFailed


class UserDetail(RetrieveView, UpdateView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_instances = IsAuthenticated()


class UserList(ListView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ("email", "username")
    permission_instances = IsAuthenticated()


class Register(CreateView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        response = self.create(request, args, kwargs)
        user = User.objects.get(email=request.data["email"])
        return Response(
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "token": user.auth_token.key,
            }
        )
