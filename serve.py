from flask import (
    Flask, 
    request
)

import socket

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def seed():
    if request.method == 'POST': 
        subprocess.Popen(['python3', 'stress_cpu.py'])
    elif request.method == 'GET': 
        return str(socket.gethostname())
    else: 
        return 'Method is not supported.'

if __name__ == "__main__":
    app.run()