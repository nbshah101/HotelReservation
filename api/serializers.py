from rest_framework import serializers
from .models import ReservationList

class ReservationListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ReservationList
        fields = ('id', 'name', 'count', 'check_in', 'check_out', 'status')
