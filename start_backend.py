import subprocess
import sys
import os

backend_path = os.path.join(os.getcwd(), "backend")

subprocess.Popen([
    sys.executable,
    "-m",
    "uvicorn",
    "app.main:app",
    "--host",
    "127.0.0.1",
    "--port",
    "8000"
], cwd=backend_path)
