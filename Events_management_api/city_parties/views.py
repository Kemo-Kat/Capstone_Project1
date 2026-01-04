from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Event
from .serializers import EventSerializer, UserSerializer
from django.http import JsonResponse
from django.shortcuts import render

def city_parties(request):
    return render(request, 'city_parties.html')

def events_list(request):
    # Your logic here
    return JsonResponse({'city_parties': []})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get all upcoming events"""
        upcoming_events = Event.objects.filter(date__gte=timezone.now())
        serializer = self.get_serializer(upcoming_events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_location(self, request):
        """Filter events by location"""
        location = request.query_params.get('location', None)
        if location:
            events = Event.objects.filter(location__icontains=location, date__gte=timezone.now())
            serializer = self.get_serializer(events, many=True)
            return Response(serializer.data)
        return Response({"error": "Location parameter required"}, status=400)