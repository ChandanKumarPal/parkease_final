# from django.db import models
# from django.contrib.auth.models import User
# from datetime import timedelta

# class Slot(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     def duration(self):
#         return self.end_time - self.start_time

#     def price(self):
#         duration = self.duration()
#         hours = duration.total_seconds() // 3600
#         return 100 * hours  # 100rs per hour

#     def __str__(self):
#         return f"{self.user.username} - {self.slot.name}"


# new code and logic start from here if any error occoured user another code 


from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Slot(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    vehicle_number = models.CharField(max_length=20 , default='UNKNOWN')

    def duration(self):
        return self.end_time - self.start_time

    def price(self):
        base_price = 100  # Example base price per hour
        duration = self.duration()
        hours = duration.total_seconds() // 3600
        num_bookings = Booking.objects.filter(slot=self.slot).count()
        dynamic_price = base_price * (1 + 0.1 * num_bookings)
        return dynamic_price

    def __str__(self):
        return f"{self.user.username} - {self.slot.name}"
