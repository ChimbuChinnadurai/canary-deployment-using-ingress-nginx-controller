import socket
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def return_hostname():
    return "Host: "+ socket.gethostname() +", Version: v2.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

