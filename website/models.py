from django.db import models

# Create your models here.


class Record(models.Model):
    """Class Model"""

    # Automatically, add the time at which a record created.
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(
        max_length=250
    )  # This the recommended email maximum length.
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(
        max_length=16
    )  # As recommended, 16 should cover all cases.

    def __str__(self):
        return f"Customer {self.pk}: {self.first_name} {self.last_name}"  # pk is the primary key of the record.
