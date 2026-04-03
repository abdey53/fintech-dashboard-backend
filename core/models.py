from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=10, choices= ROLE_CHOICES, default='viewer')
    is_active = models.BooleanField(default=True)

class FinancialRecord(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense')
    )
    amount = models.FloatField()
    type = models.CharField(max_length=10, choices= TYPE_CHOICES)
    category = models.CharField(max_length=100)
    date = models.DateField()
    note = models.TextField(blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.amount}"
