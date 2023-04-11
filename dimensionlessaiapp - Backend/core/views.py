from django.shortcuts import render
from rest_framework.views import APIView
import pandas as pd
from rest_framework.response import Response
from core.models import DataTable
from core.serializers import FileUploadSerializer, FetchFileSerializer
# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer
class UploadFileView(APIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = DataTable(
                       image_name = row['image_name'],
                       objects_detected = row['objects_detected'],
                       timestamp= row["timestamp"]
                       )
            new_file.save()
        return Response({"status": "success"})

class FetchFileView(APIView):

    def get(self,request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        filtered_data = DataTable.objects.filter(timestamp__range=(start_date, end_date)).values('image_name','objects_detected','timestamp')
        serializer = FetchFileSerializer(filtered_data, many=True)
        return Response(serializer.data)
