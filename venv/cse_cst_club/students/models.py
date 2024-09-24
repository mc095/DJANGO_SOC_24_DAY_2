from django.db import models

# Create your models here.
class studentName(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    date_reported = models.DateField(null=True)
