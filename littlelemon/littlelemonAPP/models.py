from django.db import models
# Create your models here.
class Booking(models.Model):
   
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    No_of_guests = models.SmallIntegerField(6)
   


# Add code to create Menu model
class Menu(models.Model):

   Title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory=models.IntegerField(5)

