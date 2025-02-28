from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from api.models import Book
from api.serializers import BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]  # права


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
