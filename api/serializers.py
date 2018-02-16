from rest_framework import serializers
from .models import ReservationList

class ReservationListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("Incorrect check_out")
        return data

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ReservationList
        fields = ('id', 'name', 'count', 'check_in', 'check_out', 'status')
