import os
import sys
import time
import psutil
import subprocess
import pygetwindow
import pyautogui as p
from dotenv import load_dotenv

print('Service running...')

load_dotenv()

VPN_PATH = os.getenv('VPN_PATH')
SERVER = os.getenv('SERVER')    
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
DOMAIN = os.getenv('DOMAIN')

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == 'NEGui.exe':
        proc.kill()

time.sleep(3)
subprocess.Popen(VPN_PATH)
time.sleep(3)

window = pygetwindow.getWindowsWithTitle('NetExtender')[0]
window.activate()
time.sleep(3)

p.moveTo(1000, 400)
p.click()

print('Move the mouse to exit.')

list = [ SERVER, USER_NAME, PASSWORD, DOMAIN ]

for data in list:
    x, y = p.position()
    if x != 1000 or y != 400:
        print('Service finished by user.')
        sys.exit()

    p.keyDown('tab')
    p.hotkey('ctrl', 'a')
    p.write(data)
    time.sleep(2)

p.keyDown('enter')
print('Connecting to server')