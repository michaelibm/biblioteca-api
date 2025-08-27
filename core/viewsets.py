from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core import models, serializers, filters


# class viewsets.ModelViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filterset_class = filters.AuthorFilter
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filterset_class = filters.BookFilter
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    permission_classes = [IsAuthenticated]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer
    filterset_class = filters.LoanFilter
    permission_classes = [IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filterset_class = filters.AddressFilter
    permission_classes = [IsAuthenticated]


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer
    filterset_class = filters.PhoneFilter
    permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filterset_class = filters.ProfileFilter
    permission_classes = [IsAuthenticated]
