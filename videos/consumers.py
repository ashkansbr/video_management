import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UploadProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "upload_progress"
        self.room_group_name = "upload_progress_group"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        progress = data.get('progress')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'progress_update',
                'progress': progress
            }
        )

    async def progress_update(self, event):
        progress = event['progress']
        await self.send(text_data=json.dumps({
            'progress': progress
        }))
