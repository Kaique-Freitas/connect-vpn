import os
import sys
import time
import ifcfg
import psutil
import subprocess
import pygetwindow
import pyautogui as p
from dotenv import load_dotenv

print('Service running...')

load_dotenv()

INET_ADDRESS = os.getenv('INET_ADDRESS')
VPN_PATH = os.getenv('VPN_PATH')
SERVER = os.getenv('SERVER')    
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
DOMAIN = os.getenv('DOMAIN')

print('Verifying network requirements...')

for name, interface in ifcfg.interfaces().items(): 
    if('SonicWall NetExtender' in name and interface['inet'] == INET_ADDRESS):
        print('VPN is already connected.')
        sys.exit()

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == 'NEGui.exe':
        proc.kill()

time.sleep(2)
subprocess.Popen(VPN_PATH)
time.sleep(1)

window = pygetwindow.getWindowsWithTitle('NetExtender')[0]
window.activate()
time.sleep(1)

p.moveTo(1000, 400)
p.click()

list = [ SERVER, USER_NAME, PASSWORD, DOMAIN ]

for data in list:
    p.keyDown('tab')
    p.hotkey('ctrl', 'a')
    p.write(data)
    time.sleep(2)

p.keyDown('enter')
print('Connecting to server...')
time.sleep(6)

window.close()

print('Service finished.')