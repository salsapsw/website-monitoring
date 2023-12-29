from django.db import models

class MonitoringUpperAndLower(models.Model):
    vibration_X_upper = models.FloatField(default=5.0)
    vibration_X_lower = models.FloatField(default=0.0)
    vibration_Y_upper = models.FloatField(default=5.0)
    vibration_Y_lower = models.FloatField(default=0.0)
    vibration_Z_upper = models.FloatField(default=5.0)
    vibration_Z_lower = models.FloatField(default=0.0)
    current_upper = models.FloatField(default=0.3)
    current_lower = models.FloatField(default=0.0)
    temperature_upper = models.FloatField(default=30.0)
    temperature_lower = models.FloatField(default=0.0)
    
    cal_vibration_X = models.FloatField(default=0.0)
    cal_vibration_Y = models.FloatField(default=0.0)
    cal_vibration_Z = models.FloatField(default=0.0)
