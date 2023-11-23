from ddcutil import set_vcp, get_vcp

class GenericMonitor:
    monitor_name: str = "GenericMonitor"
    brightness_vcp: int = 0x10
    contrast_vcp: int = 0x12
    input_source_vcp: int = 0x60
    volume_vcp: int = 0x62
    video_gain_red_vcp: int = 0x16
    video_gain_green_vcp: int = 0x18
    video_gain_blue_vcp: int = 0x1A

    def __init__(self, i2c_bus: int):
        self.i2c_bus = i2c_bus

    def set_brightness(self, value: int):
        return set_vcp(self.i2c_bus, self.brightness_vcp, value)
    
    def get_brightness(self):
        return get_vcp(self.i2c_bus, self.brightness_vcp)
    
    def set_contrast(self, value: int):
        return set_vcp(self.i2c_bus, self.contrast_vcp, value)
    
    def get_contrast(self):
        return get_vcp(self.i2c_bus, self.contrast_vcp)
    
    def set_input_source(self, value: int):
        return set_vcp(self.i2c_bus, self.input_source_vcp, value)
    
    def get_input_source(self):
        return get_vcp(self.i2c_bus, self.input_source_vcp)
    
    def set_volume(self, value: int):
        return set_vcp(self.i2c_bus, self.volume_vcp, value)
    
    def get_volume(self):
        return get_vcp(self.i2c_bus, self.volume_vcp)
    
    def set_video_color_gain_red(self, value: int):
        return set_vcp(self.i2c_bus, self.video_gain_red_vcp, value)
    
    def get_video_color_gain_red(self):
        return get_vcp(self.i2c_bus, self.video_gain_red_vcp)
    
    def set_video_color_gain_green(self, value: int):
        return set_vcp(self.i2c_bus, self.video_gain_green_vcp, value)
    
    def get_video_color_gain_green(self):
        return get_vcp(self.i2c_bus, self.video_gain_green_vcp)
    
    def set_video_color_gain_blue(self, value: int):
        return set_vcp(self.i2c_bus, self.video_gain_blue_vcp, value)
    
    def get_video_color_gain_blue(self):
        return get_vcp(self.i2c_bus, self.video_gain_blue_vcp)
    
    def get_monitor_name(self):
        return self.monitor_name
    
