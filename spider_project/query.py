import os
from time import perf_counter

import django
from django.conf import settings
from django.contrib.gis.geos import Point
import psycopg

# Set up the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spider_project.settings')
django.setup()

from spider_app.models import SOVBuilding


def raw_sql_query_caller(customer_latlng, radius, top_x):
    raw_query_sum = raw_query = """
        SELECT
            SUM(tiv)
        FROM
            spider_app_sovbuilding
        WHERE 
            ST_DistanceSphere(point_field, ST_GeomFromEWKB(%s)) < %s
        """

    raw_query = """
        SELECT
            MAX(tiv), SUM(tiv), ST_AsText(point_field), ST_DistanceSphere(point_field, ST_GeomFromEWKB(%s)) as distance
        FROM
            spider_app_sovbuilding
        WHERE 
            ST_DistanceSphere(point_field, ST_GeomFromEWKB(%s)) < %s

        GROUP BY 
            point_field

        ORDER BY
            MAX(tiv) DESC
        LIMIT %s
        """
    # ORDER BY
    #     tiger_coastline.line_field <-> ST_GeomFromEWKB(%s)
    # LIMIT 1

    db = settings.DATABASES['default']
    data = customer_latlng.ewkb
    with psycopg.Connection.connect(
        **{
            "user": db['USER'],
            "password": db['PASSWORD'],
            "dbname": db['NAME'],
            "host": db['HOST'],
            "port": db['PORT'],
        }
    ) as conn:
        with conn.cursor() as cur:
            start = perf_counter()
            cur.execute(raw_query, [data, data, radius, top_x])
            output = cur.fetchall()
            end = perf_counter()
            print(f"Top {top_x}: {end-start}s\n")

            start = perf_counter()
            cur.execute(raw_query_sum, [data, radius])
            tiv = cur.fetchall()
            end = perf_counter()
            print(f"Top {top_x}: {end-start}s\n")

    print(f"Total tiv within the radius {tiv}")
    for i in output:
        print(i)

    return output


if __name__ == "__main__":
    latitude = 37.7749
    longitude = -122.4194

    customer_latlng = Point(x=longitude, y=latitude, srid=4326)
    radius = 100
    top_x = 5

    data = raw_sql_query_caller(customer_latlng, radius, top_x)
