# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:25:17 2024

@author: JinQiuyi
"""
from typing import List
from fastapi import FastAPI,WebSocket,WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        
manager = ConnectionManager() 

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast("{}: {}".format(username, data))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
