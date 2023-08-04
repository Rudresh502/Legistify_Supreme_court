from django.db import models

# Create your models here.

class Final_list(models.Model):
    date_of_hearing = models.DateField()
    description = models.TextField()
    pdf_link = models.TextField()

