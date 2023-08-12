from django.db import models

# Create your models here.

class NewDonor(models.Model):
    full_name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    dob = models.CharField(max_length=50, blank=True)
    pnumber = models.CharField(max_length=50, blank=True)
    gender  = models.CharField(max_length=50, blank=True)
    email  = models.CharField(max_length=50, blank=True)
    blood_group  = models.CharField(max_length=50, blank=True)
    city  = models.CharField(max_length=50, blank=True)
    home_address  = models.CharField(max_length=1000, blank=True)
    nationality  = models.CharField(max_length=1000, blank=True)
    marital  = models.CharField(max_length=1000, blank=True)
    state_of_origin  = models.CharField(max_length=1000, blank=True)
    lga  = models.CharField(max_length=1000, blank=True)
    question  = models.CharField(max_length=1000, blank=True)
    birthday_check  = models.CharField(max_length=50, blank=True)
    due_date  = models.CharField(max_length=50, blank=True)
    date  = models.CharField(max_length=50, blank=True)
    count  = models.IntegerField(blank=True)

    def __str__(self):
        return self.full_name
    

class StockIncrease(models.Model):
    blood_group = models.CharField(max_length=50, blank=True)
    unit = models.IntegerField(blank=True)
    month = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.blood_group
    
class History(models.Model):
    blood_group = models.CharField(max_length=50, blank=True)
    unit = models.IntegerField(blank=True)
    month = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.blood_group
