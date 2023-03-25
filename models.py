from django.db import models


class EnquiryType(models.Model):
    id = models.BigAutoField(primary_key=True)
    enquiry_type = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.enquiry_type

class Enquiry(models.Model):
    id = models.BigAutoField(primary_key=True)
    enquiry_type = models.ForeignKey(EnquiryType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=30)
    email = models.EmailField()
    notes = models.TextField()