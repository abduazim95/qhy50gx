from enum import Enum

class Commands(Enum):
    CONTROL_BRIGHTNESS = 0     # image brightness
    CONTROL_CONTRAST = 1       # image contrast 
    CONTROL_WBR = 2            # red of white balance 
    CONTROL_WBB = 3            # blue of white balance
    CONTROL_WBG = 4            # the green of white balance 
    CONTROL_GAMMA = 5          # screen gamma 
    CONTROL_GAIN = 6           # camera gain 
    CONTROL_OFFSET = 7         # camera offset 
    CONTROL_EXPOSURE = 8       # expose time (us)
    CONTROL_SPEED = 9          # transfer speed 
    CONTROL_TRANSFERBIT = 10    # image depth bits 
    CONTROL_CHANNELS = 11       # image channels 
    CONTROL_USBTRAFFIC = 12     # hblank 
    CONTROL_ROWNOISERE = 13     # row denoise 
    CONTROL_CURTEMP = 14        # current cmos or ccd temprature 
    CONTROL_CURPWM = 15         # current cool pwm 
    CONTROL_MANULPWM = 16       # set the cool pwm 
    CONTROL_CFWPORT = 17        # control camera color filter wheel port 
    CONTROL_COOLER = 18         # check if camera has cooler
    CONTROL_ST4PORT = 19        # check if camera has st4port
    CAM_COLOR = 20
    CAM_BIN1X1MODE = 21         # check if camera has bin1x1 mode 
    CAM_BIN2X2MODE = 22         # check if camera has bin2x2 mode 
    CAM_BIN3X3MODE = 23         # check if camera has bin3x3 mode 
    CAM_BIN4X4MODE = 24         # check if camera has bin4x4 mode 
    CAM_MECHANICALSHUTTER = 25                   # mechanical shutter  
    CAM_TRIGER_INTERFACE = 26                    # triger  
    CAM_TECOVERPROTECT_INTERFACE = 27            # tec overprotect
    CAM_SINGNALCLAMP_INTERFACE = 28              # singnal clamp 
    CAM_FINETONE_INTERFACE = 29                  # fine tone 
    CAM_SHUTTERMOTORHEATING_INTERFACE = 30       # shutter motor heating 
    CAM_CALIBRATEFPN_INTERFACE = 31              # calibrated frame 
    CAM_CHIPTEMPERATURESENSOR_INTERFACE = 32     # chip temperaure sensor
    CAM_USBREADOUTSLOWEST_INTERFACE = 33         # usb readout slowest 

    CAM_8BITS = 34                               # 8bit depth 
    CAM_16BITS = 35                              # 16bit depth
    CAM_GPS = 36                                 # check if camera has gps 

    CAM_IGNOREOVERSCAN_INTERFACE = 37            # ignore overscan area 

    QHYCCD_3A_AUTOBALANCE = 38
    QHYCCD_3A_AUTOEXPOSURE = 39
    QHYCCD_3A_AUTOFOCUS = 40
    CONTROL_AMPV = 41                            # ccd or cmos ampv
    CONTROL_VCAM = 42                           # Virtual Camera on off 