from django.db import models
from django.contrib.auth.models import User


# PetType models is defineting
class PetType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


#Advert model is defineting
class Advert(models.Model):
    region = models.CharField(max_length=255)
    pet_type = models.ForeignKey("PetType")
    user = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date_created = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s -> %s" % (self.pet_type, self.user.name)


# PetType model is defineting
class PetType(models.Model):
    pass