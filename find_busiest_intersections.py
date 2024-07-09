
"""
Module to find the busiest intersections in a smart city.

"""

def find_busiest_intersections(traffic_data):
    """
    Finds the intersections with the highest number of vehicles.

    Parameter : traffic_data : A dictionary where keys are intersection names and values are the number of vehicles.

    Returns: list : A list of intersection with the highest number of vehicles
    """
    if not traffic_data:
        return []
    
    max_vehicles = max(traffic_data.values())
    busiest_intersections = [intersection for intersection, vehicles in traffic_data.items() if vehicles == max_vehicles]

    print(f"Intersections with the highest number of vehicles ({max_vehicles}):")
    for intersection in busiest_intersections:
        print(intersection)

    return busiest_intersections