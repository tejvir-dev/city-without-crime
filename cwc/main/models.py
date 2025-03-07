from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LoginMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class PoliceStationMaster(models.Model):
    police_station_name = models.CharField(max_length=100)
    police_station_id = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    police_station_head = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.police_station_name

class Emergency(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Complaint(models.Model):
    choices = [("Pending", "Pending"), ("In Progress", "In Progress"), ("Resolved", "Resolved"), ("Rejected", "Rejected")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=choices, default="Pending")
    p_id = models.ForeignKey(PoliceStationMaster, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
    
class CriminalMaster(models.Model):
    gen = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    stat = [("Arrested", "Arrested"), ("In Custody", "In Custody"), ("Released", "Released"), ("On Bail", "On Bail"), ("Wanted", "Wanted")]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gen)
    height = models.FloatField()
    weight = models.FloatField()
    level = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    status = models.CharField(max_length=20, choices=stat)
    criminal_picture = models.ImageField(upload_to="criminals/")
    
    def __str__(self):
        return f"{self.name} - {self.status}"