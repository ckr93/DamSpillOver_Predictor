from django.db import models

# Create your models here.
class Person(models.Model):
    id=models.CharField(max_length=200,blank = True,null = True, )
    record_id=models.CharField(max_length=200, null=False ,primary_key=True)
    Year=models.CharField(max_length=200)
    Month=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    Elevation=models.CharField(max_length=200)
    Storage=models.CharField(max_length=200)
    Presentage=models.CharField(max_length=200)
    Power=models.CharField(max_length=200)
    Energy=models.CharField(max_length=200)
    Outlet=models.CharField(max_length=200)
    Spill=models.CharField(max_length=200)
    Inflow=models.CharField(max_length=200)
    Rainfall=models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Year, self.Month, self.Date, self.Elevation, self.Storage, self.Presentage, self.Power, self.Energy, self.Spill, self.Inflow, self.Rainfall