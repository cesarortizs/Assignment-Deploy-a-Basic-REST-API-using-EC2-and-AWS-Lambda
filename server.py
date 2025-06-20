from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/status")
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return str(uptime_seconds) + " seconds"