from django.db import models

class MonitoringUpperAndLower(models.Model):
    vibration_upper = models.FloatField(default=5.0)
    vibration_lower = models.FloatField(default=0.0)
    current_upper = models.FloatField(default=0.3)
    current_lower = models.FloatField(default=0.0)
    temperature_upper = models.FloatField(default=30.0)
    temperature_lower = models.FloatField(default=0.0)
