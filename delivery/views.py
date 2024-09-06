from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
import airsim
import random
import requests

# Global variable to track mission status
mission_active = False

def home(request):
    return render(request, "map.html")

def drone_control(request):
    return render(request, 'drone-control.html')

def set_pickup_location(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        if lat and lon:
            # Process and store the pickup location
            return JsonResponse({'status': 'Pickup location set successfully'})
        return HttpResponseBadRequest('Invalid input')
    return HttpResponseBadRequest('Invalid request method')

def set_delivery_location(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        if lat and lon:
            # Process and store the delivery location
            return JsonResponse({'status': 'Delivery location set successfully'})
        return HttpResponseBadRequest('Invalid input')
    return HttpResponseBadRequest('Invalid request method')

# Mission control functions
def start_mission():
    global mission_active
    mission_active = True

def end_mission():
    global mission_active
    mission_active = False

def get_terrain_elevation(lat, lon):
    # Simulate terrain elevation data
    return random.uniform(0, 500)  # Simulated elevation in meters

def check_obstacles_nearby(lat, lon):
    # Simulate obstacle detection
    return random.choice([True, False])
def find_alternative_landing_site(lat, lon):
    """
    Simulate finding an alternative landing site near the given lat and lon.
    This example simply shifts the latitude and longitude by a small random amount.
    In a real-world scenario, this function could use more advanced methods like querying
    a terrain map or obstacle database.
    """
    # Shift latitude and longitude by a small random value
    lat_shift = random.uniform(-0.001, 0.001)  # Slight change in latitude
    lon_shift = random.uniform(-0.001, 0.001)  # Slight change in longitude

    alternative_lat = lat + lat_shift
    alternative_lon = lon + lon_shift

    return {
        'latitude': alternative_lat,
        'longitude': alternative_lon,
        'message': 'Alternative landing site suggested'
    }


def check_terrain_and_obstacles(lat, lon):
    elevation = get_terrain_elevation(lat, lon)
    threshold = 100  # Example threshold for elevation

    if elevation > threshold:
        return False, find_alternative_landing_site(lat, lon)

    obstacles_detected = check_obstacles_nearby(lat, lon)
    if obstacles_detected:
        return False, find_alternative_landing_site(lat, lon)

    return True, None

def check_weather_conditions(lat, lon):
    # Simulate random weather conditions
    wind_speed = random.uniform(0, 20)  # Wind speed between 0 and 20 m/s
    visibility = random.uniform(1000, 10000)  # Visibility between 1000 and 10000 meters

    # Return the weather data and suitability for flight
    return {
        'suitable': wind_speed < 10 and visibility > 5000,  # Flight is suitable if wind is < 10 and visibility > 5000
        'wind_speed': wind_speed,
        'visibility': visibility
    }

def check_conditions(request):
    if request.method == 'POST':
        pickup_lat = float(request.POST.get('pickup_lat'))
        pickup_lon = float(request.POST.get('pickup_lon'))
        delivery_lat = float(request.POST.get('delivery_lat'))
        delivery_lon = float(request.POST.get('delivery_lon'))
        check_terrain = request.POST.get('check_terrain', 'false') == 'true'
        check_weather = request.POST.get('check_weather', 'false') == 'true'

        battery_level = 85  # Example battery level (can be dynamically fetched)
        conditions_suitable = True
        reasons = []

        if check_weather:
            weather_conditions = check_weather_conditions(pickup_lat, pickup_lon)
            if not weather_conditions['suitable']:
                conditions_suitable = False
                reasons.append(f"Bad weather (Wind: {weather_conditions['wind_speed']} m/s, Visibility: {weather_conditions['visibility']} m)")

        if check_terrain:
            terrain_ok, alternative_site = check_terrain_and_obstacles(delivery_lat, delivery_lon)
            if not terrain_ok:
                conditions_suitable = False
                reasons.append('Unsafe terrain')

        if battery_level < 20:
            conditions_suitable = False
            reasons.append('Low battery')

        if conditions_suitable:
            return JsonResponse({'suitable': True})
        else:
            return JsonResponse({'suitable': False, 'reasons': reasons})
    return HttpResponseBadRequest('Invalid request method')


def takeoff(request):
    global mission_active
    client = airsim.MultirotorClient(ip="172.30.16.1", port=41451)
    client.confirmConnection()

    # Check battery level before takeoff
    # Uncomment when battery method is available
    # battery_level = client.getBatteryCharge()
    # if battery_level < 20:
    #     return JsonResponse({'status': 'Battery too low for takeoff'}, status=400)

    # Arm the drone and takeoff
    client.armDisarm(True)
    client.takeoffAsync().join()

    # Extract the delivery location from the request
    x = float(request.GET.get('x', 0))  # X coordinate (latitude)
    y = float(request.GET.get('y', 0))  # Y coordinate (longitude)
    z = float(request.GET.get('z', -10))  # Z coordinate (altitude, -10 for altitude)

    # Move to the specified delivery location
    client.moveToPositionAsync(x, y, z, 5).join()

    # Mark the mission as active
    start_mission()

    return JsonResponse({'status': f'Drone taken off and moved to ({x}, {y}, {z})'})


def get_drone_status(request):
    global mission_active
    
    if mission_active:
        client = airsim.MultirotorClient(ip="172.30.16.1", port=41451)
        client.confirmConnection()
        state = client.getMultirotorState()
        position = state.kinematics_estimated.position
        return JsonResponse({
            'location': {
                'lat': position.x_val,
                'lon': position.y_val,
                'alt': position.z_val
            },
            #'battery': client.getBatteryCharge(),
            'mission_status': 'In Progress'
        })
    else:
        return JsonResponse({'error': 'No active mission'}, status=400)

def move_to_position(request):
    global mission_active
    client = airsim.MultirotorClient(ip="172.30.16.1", port=41451)
    client.confirmConnection()

    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))
    z = float(request.GET.get('z', 0))
    client.moveToPositionAsync(x, y, z, 5).join()

    # Mark the mission as active
    start_mission()

    return JsonResponse({'status': f'Drone moved to ({x}, {y}, {z})'})

def end_mission_view(request):
    global mission_active
    
    # End the mission when this view is called
    end_mission()
    
    return JsonResponse({'status': 'Mission ended'})
