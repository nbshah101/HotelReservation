from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import ReservationListSerializer
from .models import ReservationList
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ReservationList.objects.all()
    serializer_class = ReservationListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


@method_decorator(csrf_exempt, name='dispatch')
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT requests."""

    queryset = ReservationList.objects.all()
    serializer_class = ReservationListSerializer