from rest_framework import serializers
from . import models


class ScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ('id', 'name')


class SeatSerializer(serializers.ModelSerializer):

    screen = ScreenSerializer(read_only=True)

    class Meta:
        model = models.Seat
        fields = ('id', 'screen', 'row', 'seat_number', 'is_aisle_seat', 'is_reserved')




