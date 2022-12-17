from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from api.models import *
from api.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """The API endpoint for CRUD operations on User Model"""
    
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
