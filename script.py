import pyautogui as p
import time
import subprocess
import pygetwindow
import os
import psutil
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

list = [ SERVER, USER_NAME, PASSWORD, DOMAIN ]

for data in list:
    p.keyDown('tab')
    p.hotkey('ctrl', 'a')
    p.write(data)
    time.sleep(2)

p.keyDown('enter')
print('Connection...')