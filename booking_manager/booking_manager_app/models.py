from django.db import models


class DateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Screen(DateTimeBase):

    name = models.CharField(max_length=20, unique=True)


class Seat(DateTimeBase):

    screen = models.ForeignKey(Screen, related_name="seats", on_delete=models.CASCADE)
    row = models.CharField(max_length=4)
    seat_number = models.IntegerField()
    is_aisle_seat = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)




