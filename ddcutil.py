import os
import subprocess
ddcutil_path = "/usr/bin/ddcutil"

def set_vcp(i2c_bus: int, vcp: int, value: int):
    return os.system(ddcutil_path + " --bus " + str(i2c_bus) + " setvcp " + hex(vcp) + " " + str(value))

def get_vcp(i2c_bus: int, vcp: int):
    # > ddcutil getvcp 0x10 --terse
    # VCP 10 C 0 100
    return subprocess.check_output(ddcutil_path + " --bus " + str(i2c_bus) + " getvcp " + hex(vcp) + " --terse", shell=True).decode("utf-8").split(" ")