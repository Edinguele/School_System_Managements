from django.db import models
from teachers.models import Teacher

class Timetable(models.Model):
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday')
    ])
    period = models.IntegerField()
    subject = models.CharField(max_length=100)
    classroom = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} - Period {self.period} - {self.subject}"