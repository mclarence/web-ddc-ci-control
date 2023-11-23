# Application to control monitor DDC/CI settings from web ui.
import os
from flask import Flask, render_template, request
from monitors.GenericMonitor import GenericMonitor

app = Flask(__name__)
ddcutil_path = "/usr/bin/ddcutil"
i2c_bus = "2"
monitor = GenericMonitor(int(i2c_bus))

@app.route("/")
def index():
    return render_template("index.html")

# Endpoint to set the monitor brightness using HTTP method POST
@app.route("/set_brightness", methods=["POST"])
def set_brightness():
    brightness = request.form.get("brightness")

    #sanitize input
    try:
        if int(brightness) < 0:
            brightness = "0"
        elif int(brightness) > 100:
            brightness = "100"
    except ValueError:
        return "Bad Request", 400

    status = monitor.set_brightness(brightness)

    # check if the return code is 0
    if status == 0:
        return "OK", 200
    else:
        return "ERROR", 500
    
@app.route("/set_input", methods=["POST"])
def set_input():
    input = request.form.get("input")

    #sanitize input
    if input == "HDMI-1":
        input = 0x11
    elif input == "HDMI-2":
        input = 0x12
    else:
        return "Bad Request", 400

    status = monitor.set_input_source(input)

    # check if the return code is 0
    if status == 0:
        return "OK", 200
    else:
        return "ERROR", 500

if __name__ == "__main__":
    app.run(debug=True)