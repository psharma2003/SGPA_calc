# models.py
from django.db import models

class StudentGrade(models.Model):
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=4)  # Assuming grades are represented as strings like 'A', 'B', etc.
