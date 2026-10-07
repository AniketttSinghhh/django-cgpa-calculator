from django.db import models
from django.contrib.auth.models import User

class CGPARecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_credits = models.FloatField()
    cgpa = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CGPA: {self.cgpa} ({self.created_at.strftime('%Y-%m-%d')})"
