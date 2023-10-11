from django.db import models

class MonitoringUpperAndLower(models.Model):
    vibration_upper = models.IntegerField(default=1000)
    vibration_lower = models.IntegerField(default=0)
    current_upper = models.IntegerField(default=1)
    current_lower = models.IntegerField(default=0)
    temperature_upper = models.IntegerField(default=1000)
    temperature_lower = models.IntegerField(default=0)
