from django.contrib.gis.db import models


class SOVBuilding(models.Model):
    tiv = models.BigIntegerField()
    point_field = models.PointField(srid=4326)
    extra_data = models.JSONField(default=dict)
