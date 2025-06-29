from rest_framework import serializers
from .models import Bus, seat
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class seatSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat
        fields = ['id','seat_number', 'is_booked', 'bus']



