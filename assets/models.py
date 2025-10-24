from django.db import models
from django.utils import timezone

# Create your models here. 
class Assets(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    purchase_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.pk