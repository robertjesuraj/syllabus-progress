from django.db import models
from django.urls import reverse
# from django.utils import date
import datetime

# Create your models here.

class Syllabus(models.Model):
    
    syllabus_text = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    proposed_date_completeion = models.DateField(blank=False)
    completion_status = models.IntegerField(default=0)
    # created_date = models.DateTimeField('date created')

    # def __init__(self):
    #     self.created_date = datetime.datetime.now()

    def __str__(self):
        return self.syllabus_text
    
    def get_absolute_url(self):
        return reverse('kichu:syllabus_edit', kwargs={'pk': self.pk})