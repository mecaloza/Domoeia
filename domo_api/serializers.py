from rest_framework import serializers



class LocationSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name_location = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()
7
class DeviceSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name_device = serializers.CharField(max_length=255)
    unit =  serializers.CharField(max_length=255)
    location_id = serializers.IntegerField()

class DotsSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    value = serializers.FloatField()
    datTime =  serializers.DateTimeField()
    device_id = serializers.IntegerField()