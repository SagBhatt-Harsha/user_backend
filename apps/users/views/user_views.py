from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import UserProfile
from apps.users.serializers import UserProfileSerializer

class CreateUserProfileViewSet(viewsets.ModelViewSet):
    '''Handles All HTTP Methods that can be used with User Profile'''
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    lookup_field = "unique_id"
    # Otherwise api/users/<id> would have the Auto-id, Not the UUID.


    

        