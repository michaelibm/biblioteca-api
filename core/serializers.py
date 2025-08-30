from rest_framework import serializers
from core import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address  # <-- sem aspas
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loan
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'