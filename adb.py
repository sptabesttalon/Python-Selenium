import time
import subprocess
id_device='emulator-5554'

def adb_click(coord_x,coord_y):
    adb_command='adb -s %s shell input tap %s %s'%(id_device,coord_x,coord_y)
    subprocess.call(adb_command)

def adb_send_text(text):
    adb_command='adb -s %s shell input text %s'%(id_device,text)
    subprocess.call(adb_command)

# def screen_capture()
#     adb_command='adb -s {device_id} shell screencap -p /sdcard/screencap{index}.png && adb pull /sdcard/screencap{index}.png  D:\LDPlayer'

# adb_click(228,138)
# adb_send_text('nghia%snghiahsgs')

# time.sleep()