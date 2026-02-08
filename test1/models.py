from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.full_name

class Vehicle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_number

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()
    latitude = models.DecimalField(max_digits=10)
    longitude = models.DecimalField(max_digits=10)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "location"

    def __str__(self):
        return self.location_name


class ParkingSlot(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=10)
    slot_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "parking_slot"

    def __str__(self):
        return self.slot_number



class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_status = models.CharField(max_length=20)

    class Meta:
        db_table = "booking"

    def __str__(self):
        return self.booking_status


class Payment(models.Model):
    booking = models.OneToOneField(Booking,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_mode = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payment"

    def __str__(self):
        return slef.payment_status