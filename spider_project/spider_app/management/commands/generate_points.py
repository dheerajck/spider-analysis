import math
import random


"""
# Starting coordinate (latitude, longitude)
start_lat = 37.7749
start_lon = -122.4194

# Bearing in degrees (0 = north, 90 = east, etc.)
bearing = 0

# Distance in meters from starting point
distance = 10

# Earth radius in meters
earth_radius = 6371000

start_lat_rad = math.radians(start_lat)
start_lon_rad = math.radians(start_lon)


# Calculate new latitude and longitude coordinates
new_lat_rad = math.asin(
    math.sin(start_lat_rad) * math.cos(distance / earth_radius) + math.cos(start_lat_rad) * math.sin(distance / earth_radius) * math.cos(bearing_rad)
)
new_lon_rad = start_lon_rad + math.atan2(
    math.sin(bearing_rad) * math.sin(distance / earth_radius) * math.cos(start_lat_rad),
    math.cos(distance / earth_radius) - math.sin(start_lat_rad) * math.sin(new_lat_rad),
)

# Convert new coordinates to degrees
new_lat = math.degrees(new_lat_rad)
new_lon = math.degrees(new_lon_rad)

# Print new coordinates
print(f"New coordinates: ({new_lat}, {new_lon})") 
"""


def generate_points(start_lat=37.7749, start_lon=-122.4194, n=500):
    # Earth radius in meters
    earth_radius = 6371000

    start_lat_rad = math.radians(start_lat)
    start_lon_rad = math.radians(start_lon)

    data = []
    for i in range(n):
        bearing = random.randint(0, 360)
        bearing_rad = math.radians(bearing)

        tiv = random.choice([(i // 50) + 1, (i // 50) + 2, (i // 50) + 3, (i // 50) + 4, (i // 50) + 5])

        distance = random.randint(50 * (i // 100), 50 * (i // 100) + 1)

        new_lat_rad = math.asin(
            math.sin(start_lat_rad) * math.cos(distance / earth_radius)
            + math.cos(start_lat_rad) * math.sin(distance / earth_radius) * math.cos(bearing_rad)
        )
        new_lon_rad = start_lon_rad + math.atan2(
            math.sin(bearing_rad) * math.sin(distance / earth_radius) * math.cos(start_lat_rad),
            math.cos(distance / earth_radius) - math.sin(start_lat_rad) * math.sin(new_lat_rad),
        )
        new_lat = math.degrees(new_lat_rad)
        new_lon = math.degrees(new_lon_rad)
        data.append({'lat': new_lat, 'long': new_lon, 'tiv': tiv})

    return data
