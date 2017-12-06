from casino_finder.models import Casino
from casino_finder.serializers import CasinoSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render
from rest_framework import generics
import geocoder

# Create your views here.

class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer

    #after installing geocoder add this
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g = geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        serializer.save(location=pnt)

    #overriding get queryset
    def get_queryset(self):
        qs = super().get_queryset() #return a default queryset, gets the objects of Casino.Objects.all()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('long', None)

        if latitude and longitude:
            pnt = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)
            qs = qs.annotate(distance=Distance('location', pnt)).order_by('distance')
        return qs