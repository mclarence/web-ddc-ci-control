# Web DDC/CI Control
Control monitor's DDCCI via web interface. Currently can change brightness and input.

## Requirements
* Python 3.11+ (Lower untested)
* Flask

## Installation
1. Install Python 3.11+
2. Install requirements.
```
pip install flask gunicorn
```
3. Install ddcutil and ensure that your user has permission to access the I2C bus.
4. Clone this repository.
5. Edit app.py and change the following lines:
```
ddcutil_path = "/usr/bin/ddcutil" # Path to ddcutil
i2c_bus = "1" # I2C bus number
```
6. Run the app.
```
gunicorn -b 0.0.0.0 app:app
```