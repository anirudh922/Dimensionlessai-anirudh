from django.db import models


class DataTable(models.Model):
    image_name = models.CharField(max_length=1000)
    objects_detected = models.CharField(max_length=1000)
    timestamp = models.DateField()

    class Meta:
        managed = True
        db_table = "core_datatable"
    
    def __str__(self):
        return f"{self.image_name} - {self.objects_detected} - {self.timestamp}"
