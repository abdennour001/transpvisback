from rest_framework.generics import GenericAPIView
from rest_framework import mixins


class ListView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveView(mixins.RetrieveModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)