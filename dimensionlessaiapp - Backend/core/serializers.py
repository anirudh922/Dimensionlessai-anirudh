from rest_framework import serializers
from core.models import DataTable

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = DataTable
        fields = "__all__"

class FetchFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = (
            'image_name',
            'objects_detected',
            'timestamp'
        )