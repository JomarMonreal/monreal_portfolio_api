from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return "{}: {}".format(self.classification, self.name)
    