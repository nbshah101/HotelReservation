from __future__ import unicode_literals

from django.db import models

status_choice = ((1,"FUTURE RESERVATION"), (2,"CHECK-IN"), (3,"CHECK-OUT"), (4,"CANCELLED"))

class ReservationList(models.Model):
    name = models.CharField(max_length=255, blank=False)
    count = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=255, choices=status_choice, default='FUTURE RESERVATION')

    def __str__(self):
        return "{}".format(self.name)


