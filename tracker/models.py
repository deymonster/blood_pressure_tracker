from django.db import models
from django.contrib.auth.models import User

class BloodPressureRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.systolic}/{self.diastolic} on {self.date}"
