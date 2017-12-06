from casino_finder.models import Casino
from rest_framework import serializers

class CasinoSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(source='distance.mi', max_digits=10,
                                        decimal_places=2, required=False,
                                        read_only=True)
    class Meta:
        model = Casino
        fields = ('id', 'name', 'address','location','distance')
        read_only_fields = ('location',)
