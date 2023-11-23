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
    
@app.route("/get_brightness", methods=["GET"])
def get_brightness():
    brightness = monitor.get_brightness()

    return brightness, 200
    
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

@app.route("/set_contrast", methods=["POST"])
def set_contrast():
    contrast = request.form.get("contrast")

    #sanitize input
    try:
        if int(contrast) < 0:
            contrast = "0"
        elif int(contrast) > 100:
            contrast = "100"
    except ValueError:
        return "Bad Request", 400

    status = monitor.set_contrast(contrast)

    # check if the return code is 0
    if status == 0:
        return "OK", 200
    else:
        return "ERROR", 500

@app.route("/get_contrast", methods=["GET"])
def get_contrast():
    contrast = monitor.get_contrast()

    return contrast, 200

@app.route("/set_volume", methods=["POST"])
def set_volume():
    volume = request.form.get("volume")

    #sanitize input
    try:
        if int(volume) < 0:
            volume = "0"
        elif int(volume) > 100:
            volume = "100"
    except ValueError:
        return "Bad Request", 400

    status = monitor.set_volume(volume)

    # check if the return code is 0
    if status == 0:
        return "OK", 200
    else:
        return "ERROR", 500
    
@app.route("/get_volume", methods=["GET"])
def get_volume():
    volume = monitor.get_volume()

    return volume, 200
    
@app.route("/set_video_color_gain", methods=["POST"])
def set_video_color_gain():
    red = request.form.get("red")
    green = request.form.get("green")
    blue = request.form.get("blue")

    #sanitize input
    try:
        if int(red) < 0:
            red = "0"
        elif int(red) > 100:
            red = "100"
    except ValueError:
        return "Bad Request", 400

    try:
        if int(green) < 0:
            green = "0"
        elif int(green) > 100:
            green = "100"
    except ValueError:
        return "Bad Request", 400

    try:
        if int(blue) < 0:
            blue = "0"
        elif int(blue) > 100:
            blue = "100"
    except ValueError:
        return "Bad Request", 400

    status = monitor.set_video_color_gain_red(int(red))
    status = monitor.set_video_color_gain_green(int(green))
    status = monitor.set_video_color_gain_blue(int(blue))

    # check if the return code is 0
    if status == 0:
        return "OK", 200
    else:
        return "ERROR", 500
    
@app.route("/get_video_color_gain", methods=["GET"])
def get_video_color_gain():
    red = monitor.get_video_color_gain_red()
    green = monitor.get_video_color_gain_green()
    blue = monitor.get_video_color_gain_blue()

    return red + " " + green + " " + blue, 200
    


if __name__ == "__main__":
    app.run(debug=True)