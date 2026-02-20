from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import List, Dict
import json

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        # Map match_id to list of active websockets
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, match_id: int):
        await websocket.accept()
        if match_id not in self.active_connections:
            self.active_connections[match_id] = []
        self.active_connections[match_id].append(websocket)

    def disconnect(self, websocket: WebSocket, match_id: int):
        if match_id in self.active_connections:
            self.active_connections[match_id].remove(websocket)
            if not self.active_connections[match_id]:
                del self.active_connections[match_id]

    async def broadcast(self, message: str, match_id: int):
        if match_id in self.active_connections:
            for connection in self.active_connections[match_id]:
                await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/{match_id}")
async def websocket_endpoint(websocket: WebSocket, match_id: int):
    # In a real app, you would validate the user here (e.g. check cookie or query param token)
    # Since WebSocket standard headers don't support custom headers easily for auth in browser JS
    await manager.connect(websocket, match_id)
    try:
        while True:
            data = await websocket.receive_text()
            # Here you would save the message to DB
            # message_data = json.loads(data)
            # await save_message_to_db(match_id, message_data)
            await manager.broadcast(data, match_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, match_id)
