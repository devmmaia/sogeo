from django.shortcuts import render

# from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def home(request):
    env = "Development" if settings.DEBUG else "PRODUCTION"
    context = {"frase": "Hello World HEROKU", "env": env}
    return render(request, "core/index.html", context)
