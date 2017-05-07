"""
A1: 21.014156, 105.841421
A2: 21.015778, 105.841324
Distant: 180m
lat: .001622
B1: 21.003088, 105.859261
B2: 21.003102, 105.864344
Distant: 550m
lng: .005083
"""

LAT_PER_100M = 0.001622/1.8
LONG_PER_100M = 0.005083/5.5


def lat_from_met(met):
    return LAT_PER_100M * met/100.0


def long_from_met(met):
    return LONG_PER_100M * met/100


def generate_coordinate(center_point_lat, center_point_lng, radius=10000,
                        scan_radius=750):

    top = center_point_lat + lat_from_met(radius)
    left = center_point_lng - long_from_met(radius)

    bottom = center_point_lat - lat_from_met(radius)
    right = center_point_lng + long_from_met(radius)

    scan_radius_step = (lat_from_met(scan_radius),
                        long_from_met(scan_radius))
    lat = top
    lng = left
    while lat > bottom:
        while lng < right:
            yield (lat, lng)
            lng += scan_radius_step[1]
        lng = left
        lat -= scan_radius_step[0]
