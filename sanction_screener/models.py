from django.db import models

# Create your models here.
class SanctionList(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    third_name = models.CharField(max_length=255, null=True)
    #sanctionId = models.CharField(max_length=255),
    reference_number = models.CharField(max_length=255, null=True)
    date_listed = models.CharField(max_length=255, null=True)#DateField(null=True)
    comments1 = models.TextField(null=True)
    designation = models.JSONField(null=True)
    nationality = models.JSONField(null=True)
    list_type = models.JSONField(null=True)
    last_day_updated = models.JSONField(null=True)
    individual_alias = models.JSONField(null=True)
    individual_address = models.JSONField(null=True)
    date_of_birth = models.JSONField(null=True)
    place_of_birth = models.JSONField(null=True)
    individual_document = models.JSONField(null=True)

    def __str__(self):
        return self.first_name