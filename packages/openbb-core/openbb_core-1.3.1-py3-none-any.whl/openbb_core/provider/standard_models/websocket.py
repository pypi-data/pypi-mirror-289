"""WebSocket Standard Model."""

import asyncio
import json
import logging
import threading
from datetime import datetime
from typing import List

logger = logging.getLogger(__name__)

import websockets
from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams

# "wss://data.tradingview.com/socket.io/websocket?from=symbols/TVC-AT40Y/yield-curve/&date=2024_07_12-13_17"


class WebSocketQueryParams(QueryParams):
    """WebSocket Query Parameters."""

    uri: str = Field(
        description="The URI of the WebSocket server.",
    )


class WebSocketData(Data):
    """WebSocket Data."""


class WebSocketClient:
    """WebSocket Client."""

    def __init__(self, uri: str, data_model: WebSocketData):
        """Initializes the WebSocket client."""
        self.uri = uri
        self.records: List = []  # List to store validated records
        self.stop_event = threading.Event()
        self.data_model = data_model

    async def _connect(self):
        async with websockets.connect(self.uri) as websocket:
            await self._receive_data(websocket)

    async def _receive_data(self, websocket):
        while not self.stop_event.is_set():
            data = await websocket.recv()
        async with websockets.connect(self.uri) as websocket:
            logger.info("Connected to WebSocket server.")
            end_time = datetime.now() + timedelta(seconds=query.lifetime)  # type: ignore
            try:
                async for message in websocket:
                    data = json.loads(message)
                    yield data
                    if datetime.now() >= end_time:
                        break
            except websockets.exceptions.ConnectionClosed as e:
                logger.error("WebSocket connection closed.")
                raise e
            finally:
                logger.info("WebSocket connection closed.")

    def start(self):
        # Reset the stop event in case it's being restarted
        self.stop_event.clear()
        # Run the asyncio event loop in a separate thread
        threading.Thread(target=self._run_event_loop, daemon=True).start()
        print("Data is now returing to the 'records' attribute.")  # noqa: T201

    def _run_event_loop(self):
        asyncio.new_event_loop().run_until_complete(self._connect())

    def stop(self):
        self.stop_event.set()
