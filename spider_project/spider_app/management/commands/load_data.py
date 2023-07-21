from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from spider_app.models import SOVBuilding

from .generate_points import generate_points


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_list = generate_points()
        SOVBuilding.objects.all().delete()
        for data in data_list:
            point_string = Point(x=data['long'], y=data['lat'], srid=4326).wkt
            tiv = data['tiv']
            SOVBuilding.objects.create(point_field=point_string, tiv=tiv)
