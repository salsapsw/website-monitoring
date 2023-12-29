from django.db import models

# Create your models here.
class MQTTData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(default=0.0) 
    current = models.FloatField(default=0.0)
    accelvibX = models.FloatField(default=0.0)
    accelvibY = models.FloatField(default=0.0)
    accelvibZ = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.topic}: {self.payload}"
