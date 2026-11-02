from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CurrentBookings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    table_no = models.IntegerField()
    seat_no = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Table {self.table_no}, Seat {self.seat_no}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["table_no", "seat_no"],
                name="unique_table_seat"
            )
        ]