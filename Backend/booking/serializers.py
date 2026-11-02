from .models import CurrentBookings
from rest_framework import serializers

class CurrentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentBookings
        fields = ['table_no', 'seat_no']
        