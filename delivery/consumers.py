import json
from channels.generic.websocket import AsyncWebsocketConsumer
import airsim

class DroneControlConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Initialize AirSim client
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

    async def disconnect(self, close_code):
        # Disconnect from the drone when WebSocket is closed
        self.client.enableApiControl(False)
        self.client.armDisarm(False)

    async def receive(self, text_data):
        data = json.loads(text_data)
        command = data.get('command')

        if command == 'up':
            await self.client.moveByVelocityAsync(0, 0, -1, 1)
        elif command == 'down':
            await self.client.moveByVelocityAsync(0, 0, 1, 1)
        elif command == 'left':
            await self.client.moveByVelocityAsync(0, -1, 0, 1)
        elif command == 'right':
            await self.client.moveByVelocityAsync(0, 1, 0, 1)
        elif command == 'forward':
            await self.client.moveByVelocityAsync(1, 0, 0, 1)
        elif command == 'backward':
            await self.client.moveByVelocityAsync(-1, 0, 0, 1)
