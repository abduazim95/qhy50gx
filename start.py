import os
import ctypes
import numpy as np
import time
from astropy.io import fits
from commands import Commands

start_time = time.time()

DIR_NAME = os.path.dirname(os.path.realpath(__file__)) + '\\fits\\'
#include SDK
hllDll = ctypes.WinDLL ("C:\\test\\qhyccd.dll")


hllDll.InitQHYCCDResource()
hllDll.ScanQHYCCD()

id = ctypes.create_string_buffer(32)
ret = hllDll.GetQHYCCDId(0, id)
hllDll.OpenQHYCCD.restype = ctypes.POINTER(ctypes.c_int)
camhandle = hllDll.OpenQHYCCD(id)
ret = hllDll.SetQHYCCDStreamMode(camhandle,0)
ret = hllDll.InitQHYCCD(camhandle)

# Declare variable of camera parameters
chipw = ctypes.c_double()
chiph = ctypes.c_double()
pixelw = ctypes.c_double()
pixelh = ctypes.c_double()
imagew = ctypes.c_int()
imageh = ctypes.c_int()
bpp = ctypes.c_int()
channels = ctypes.c_int()
ret = hllDll.GetQHYCCDChipInfo(camhandle, ctypes.byref(chipw), ctypes.byref(chiph), ctypes.byref(imagew), ctypes.byref(imageh), ctypes.byref(pixelw), ctypes.byref(pixelh), ctypes.byref(bpp))

# Print camera parameters variable
print('ChipW = {0}'.format(str(chipw.value)))
print('ChipH = {0}'.format(str(chiph.value)))
print('Imagew = {0}'.format(str(imagew.value)))
print('imageh = {0}'.format(str(imageh.value)))
print('PixelW = {0}'.format(str(pixelw.value)))
print('PixelH = {0}'.format(str(pixelh.value)))
print('Bpp = {0}'.format(str(bpp.value)))

#hllDll.GetQHYCCDParam.restype = ctypes.c_double
#speed = hllDll.GetQHYCCDParam(camhandle, Commands.CONTROL_SPEED.value)
#print("Current speed: " + str(speed))

# Set exposure time
hllDll.SetQHYCCDParam.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_double]
ret = hllDll.SetQHYCCDParam(camhandle, Commands.CONTROL_EXPOSURE.value, 1 * 1000000)

# Set temperature
ret = hllDll.IsQHYCCDControlAvailable(camhandle, Commands.CONTROL_CURTEMP.value)
print('This function available status: ' + str(ret))
if(ret == 0):
    hllDll.GetQHYCCDParam.restype = ctypes.c_double
    temp = hllDll.GetQHYCCDParam(camhandle, Commands.CONTROL_CURTEMP.value)
    print("Current temp: " + str(temp))

#Get buffer length
length = hllDll.GetQHYCCDMemLength(camhandle)
print("Length: " + str(length))


ret = hllDll.IsQHYCCDControlAvailable(camhandle, Commands.CONTROL_SPEED.value)
print('Speed function available status: ' + str(ret))
if(ret == 0):
    hllDll.SetQHYCCDParam.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_double]
    ret = hllDll.SetQHYCCDParam(camhandle, Commands.CONTROL_SPEED.value, 1.0)


ret = hllDll.IsQHYCCDControlAvailable(camhandle, Commands.CAM_IGNOREOVERSCAN_INTERFACE.value)
print('IgnoreOverScan function available status: ' + str(ret))
if(ret == 0):
    hllDll.SetQHYCCDParam.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_double]
    ret = hllDll.SetQHYCCDParam(camhandle, Commands.CAM_IGNOREOVERSCAN_INTERFACE.value, 1.0)

time.sleep(1)
ret = hllDll.SetQHYCCDBinMode(camhandle, 1, 1)
time.sleep(1)
ret = hllDll.SetQHYCCDResolution(camhandle,0,0, int(imagew.value), int(imageh.value))
time.sleep(1)

print("Init has taken %s seconds ---" % (time.time() - start_time))

i = 0
while i < 1:
    # Start exposure async
    ret = hllDll.ExpQHYCCDSingleFrame(camhandle)
    #time.sleep(2)
    start_time = time.time()
    # Allocate memory for buffer
    ImgData = ctypes.create_string_buffer(length)
    print('Receiving')

    # Get image from camera
    ret = hllDll.GetQHYCCDSingleFrame(camhandle, ctypes.byref(imagew), ctypes.byref(imageh), ctypes.byref(bpp), ctypes.byref(channels), ImgData)
    print('Saving fits on path')
    ImgData = np.frombuffer(ImgData, dtype='<u2')
    #WRITING FITS
    ImgData = np.flip(np.reshape(np.array(ImgData), [imageh.value, imagew.value]), 1)
    #ImgData = np.reshape(np.array(ImgData), [imageh.value, imagew.value])
    name = time.strftime(DIR_NAME + "Y%Y_%h_D%d_H%H_M%M_S%S_MS" + str(time.time())[11:], time.gmtime()) + '.fits'
    #name = DIR_NAME + str(i) + '.fits'
    primary = fits.PrimaryHDU(ImgData)
    hdul = fits.HDUList([primary])
    hdul.writeto(name)
    i = i + 1


# Cancel and readout
ret = hllDll.CancelQHYCCDExposingAndReadout(camhandle)

# Finish work with camera
ret = hllDll.CloseQHYCCD(camhandle)
ret = hllDll.ReleaseQHYCCDResource()