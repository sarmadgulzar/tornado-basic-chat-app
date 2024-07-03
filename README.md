# Futuristic Chat Application

This is a real-time chat application built with Python (Tornado) backend and a sleek, futuristic HTML/CSS/JS frontend. It features WebSocket communication for instant messaging and a modern, responsive user interface.

## Features

- Real-time messaging using WebSockets
- Sleek, futuristic user interface
- Random username assignment
- Distinguishes between user's own messages and others'

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- pip (Python package manager) installed

## Installation

1. Clone this repository or download the source code.

```
git clone https://github.com/sarmadgulzar/tornado-chat-app.git
cd tornado-chat-app
```

2. Create a virtual environment (recommended):

```
python3 -m venv venv
```

3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:

```
pip install -r requirements.txt
```

## Project Structure

Ensure your project directory looks like this:

```
tornado-chat-app/
│
├── main.py
└── templates/
    └── chat.html
```

## Running the Application

1. Start the server:

```
python main.py
```

By default, the server will run on `http://localhost:8888`. You can specify a different port using the `--port` option:

```
python chat_server.py --port=8000
```

2. Open a web browser and navigate to `http://localhost:8888` (or the port you specified).

3. You should see the chat interface. The application will automatically assign you a random username.

4. Open multiple browser windows or tabs to simulate different users chatting.

## Usage

- Type your message in the input field at the bottom of the chat window.
- Press the "Send" button or hit Enter to send your message.
- Your messages will appear on the right side of the chat window.
- Messages from other users will appear on the left side.

## Customization

- To modify the user interface, edit the `chat.html` file in the `templates` directory.
- To change server behavior or add new features, modify the `chat_server.py` file.

## Troubleshooting

If you encounter any issues:

1. Ensure all prerequisites are installed correctly.
2. Check that you're running the correct Python version.
3. Verify that the `tornado` package is installed in your virtual environment.
4. Make sure no other applications are using the specified port.
