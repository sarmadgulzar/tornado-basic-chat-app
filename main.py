"""
Tornado Live Chat Server

This module implements a production-ready live chat server using Tornado.
It features WebSocket communication, random user name generation, and
robust error handling.

Author: Sarmad Gulzar
Date: 2024-07-04
"""

import asyncio
import json
import logging
import os
import random
from typing import Any, Dict, Set

import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define, options, parse_command_line

# Define command-line options
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode", type=bool)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    """
    WebSocket handler for the chat application.

    [Previous class docstring content remains unchanged]
    """

    connections: Set["ChatWebSocket"] = set()
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
        "Kathy",
        "Luke",
        "Mia",
        "Nathan",
        "Olivia",
        "Peter",
        "Quinn",
        "Rachel",
        "Sam",
        "Tina",
        "Ulysses",
        "Violet",
        "Walter",
        "Xena",
        "Yvonne",
        "Zack",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name: str = ""

    def check_origin(self, origin: str) -> bool:
        """Allow connections from any origin."""
        return True

    async def open(self):
        """Handle new WebSocket connection."""
        self.name = f"{random.choice(self.names)}{random.randint(1, 1000)}"
        self.connections.add(self)
        logger.info(f"New connection opened for {self.name}")
        await self.send_message({"type": "name", "name": self.name})

    async def on_message(self, message: str):
        """Handle incoming WebSocket message."""
        try:
            parsed = json.loads(message)
            await self.broadcast_message(self.name, parsed["message"])
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON received from {self.name}")
        except KeyError:
            logger.error(f"Invalid message format received from {self.name}")

    async def on_close(self):
        """Handle WebSocket connection closure."""
        self.connections.remove(self)
        logger.info(f"Connection closed for {self.name}")

    async def send_message(self, message: Dict[str, Any]):
        """Send a message to this WebSocket."""
        try:
            await self.write_message(json.dumps(message))
        except tornado.websocket.WebSocketClosedError:
            logger.warning(
                f"WebSocket closed when trying to send message to {self.name}"
            )

    @classmethod
    async def broadcast_message(cls, sender_name: str, message: str):
        """Broadcast a message to all connected clients."""
        for conn in cls.connections:
            await conn.send_message(
                {
                    "type": "message",
                    "name": sender_name,
                    "message": message,
                    "isSelf": sender_name == conn.name,
                }
            )


class MainHandler(tornado.web.RequestHandler):
    """Handler for the main page."""

    async def get(self):
        """Render the chat HTML page."""
        await self.render("chat.html")


def make_app() -> tornado.web.Application:
    """
    Create and configure the Tornado application.

    Returns:
        tornado.web.Application: Configured Tornado application
    """
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/websocket", ChatWebSocket),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
    )


async def main():
    """
    Main function to start the Tornado server.
    """
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    logger.info(f"Chat server is running on http://localhost:{options.port}")

    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server shutting down")
