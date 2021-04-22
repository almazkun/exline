from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class City(models.Model):
    city_id = models.IntegerField(_("City id"), unique=True)
    title = models.CharField(_("City name"), max_length=255, db_index=True)
    cached_path = models.CharField(_("Province"), max_length=255, db_index=True)
    zone = models.CharField(_("Zone"), max_length=50)
    origin = models.BooleanField(_("Origin"))
    destination = models.BooleanField(_("Destination"))
    cached_parent = models.CharField(_("Parent"), max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.city_id}: {self.title}"
