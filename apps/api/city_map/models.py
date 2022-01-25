from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PolygonField(
        _("Координаты"),
        srid=4326,
        null=True,
    )
    address = models.CharField(
        _("Адрес"),
        max_length=500,
        null=True,
    )

    @property
    def area(self):
        return self.geom.area

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
