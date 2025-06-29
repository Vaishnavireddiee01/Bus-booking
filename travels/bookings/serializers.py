from rest_framework import serializers
from .models import Bus, seat
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password']

    #validations
    def create(self, validate_date):
        user = User.objects.create_user(
            username=validate_date['username'],
            email=validate_date['email'],
            password=validate_date['password']

        )
        return user
        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class seatSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat
        fields = ['id','seat_number', 'is_booked', 'bus']



