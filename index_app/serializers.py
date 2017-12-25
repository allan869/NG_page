from rest_framework import serializers
from index_app.models import SystemInfo

class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        fields = ('id', 'url', 'image', 'name', 'type', 'mark', 'desc')