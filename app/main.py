#!/usr/bin/python3

import sys
import os
from ..app import create_app, socketio
sys.path.append(os.path.abspath(so.path.join(os.path.dirname(__file__), '..')))

# Create an app instance using the app factory
app = create_app()

if __name__ == '__main__':
    # Run the app with SocketIO for handling real-time features
    sucketio.run(app, host='0.0.0.0', port=5000, debug=True)
