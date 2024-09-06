# Drone Delivery System

## Overview

This project is a drone delivery system that integrates AirSim with PX4 on Ubuntu. It allows you to control a drone, set pickup and delivery locations, and perform various mission tasks. The system uses Django for the web interface and communicates with the drone through AirSim.

## Prerequisites

- Ubuntu 20.04 or later
- Python 3.8+
- Django 3.2+
- AirSim
- PX4
- Required Python libraries: `airsim`, `requests`

## Installation

### 1. Install PX4

1. **Clone the PX4 Firmware Repository:**
    ```bash
    git clone https://github.com/PX4/PX4-Autopilot.git
    ```

2. **Navigate to the PX4 Directory:**
    ```bash
    cd PX4-Autopilot
    ```

3. **Install Dependencies:**
    ```bash
    bash ./Tools/setup/ubuntu.sh
    ```

4. **Build PX4:**
    ```bash
    make px4_sitl_default none_iris
    ```

### 2. Install AirSim

1. **Clone the AirSim Repository:**
    ```bash
    git clone https://github.com/Microsoft/AirSim.git
    ```

2. **Navigate to the AirSim Directory:**
    ```bash
    cd AirSim
    ```

3. **Install Dependencies and Build AirSim:**
    ```bash
    ./setup.sh
    ./build.sh
    ```
### 3. Configuring Unreal Engine
Install Unreal Engine: Follow the official Unreal Engine installation guide.

1. **Setup AirSim Plugin:**

Open your Unreal Engine project.
Navigate to the "Plugins" menu and enable the "AirSim" plugin.
Configure AirSim for African Environment:

Open the AirSimSettings.json file located in your Unreal Engine project directory.
Adjust the environment settings to match the African terrain and climate.
 JSON Configuration
The config.json file contains important configuration settings for the AirSim simulation.
Make sure this file is placed in the root directory of your AirSim project.
 Running the Simulation

### 4. Set Up the Django Project

1. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Required Python Packages:**
    ```bash
    pip install django airsim requests
    ```

3. **Clone the Project Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

4. **Apply Migrations and Run the Server:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. **Access the Web Interface:**
   Open your web browser and navigate to `http://localhost:8000/` to access the map and drone control interface.

2. **Set Pickup and Delivery Locations:**
   Use the web interface to set pickup and delivery coordinates on the map.

3. **Start the Mission:**
   - Click on the "Takeoff" button to start the mission.
   - The drone will take off and move to the specified coordinates.

4. **Monitor the Mission:**
   - Check the drone's status and battery level from the web interface.
   - Move the drone to specific coordinates as needed.

5. **End the Mission:**
   - Click on the "End Mission" button to stop the current mission.

## Troubleshooting

- **Connection Issues:**
  Ensure that AirSim and PX4 are running properly and that the IP address and port configurations match.

- **Battery Level Errors:**
# this is being simulated on your views.py
  Verify that the drone's battery level is adequate for takeoff and mission execution.

- **Coordinate Errors:**
  Ensure that the coordinates provided for pickup and delivery are within the valid range and correctly formatted.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
