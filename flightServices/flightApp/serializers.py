from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re
from datetime import datetime

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightNumber(self, flightNumber):
        if not re.match(r'^[A-Z0-9]+$', flightNumber):
            raise serializers.ValidationError("Flight Number must be alphanumeric")
        return flightNumber
    
    def validate(self, data):
        if data['dateOfDeparture'] < datetime.today()   :
            raise serializers.ValidationError("Date of Departure cannot be in the past")
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'