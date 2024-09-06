import requests

def get_weather_data(city_id, api_key):
    # Define the API endpoint and parameters
    url = f"http://api.openweathermap.org/data/2.5/forecast"
    
    # Parameters for the API call
    params = {
        'id': city_id,        # City ID (for example, 524901 is Moscow's ID)
        'appid': api_key,     # Your OpenWeatherMap API key
        'units': 'metric'     # Units of measurement (metric for Celsius)
    }
    
    # Make the API call
    response = requests.get(url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        weather_data = response.json()  # Parse the JSON data
        return weather_data
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return None

# Example usage
api_key = '4e2d1032f76f6233331f62d3d42ee02d'  # Replace with your actual API key
city_id = 524901  # Moscow city ID
weather_data = get_weather_data(city_id, api_key)

if weather_data:
    print(weather_data)
