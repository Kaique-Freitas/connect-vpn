import pyautogui as p
import time
import subprocess
import pygetwindow
import os
from dotenv import load_dotenv

load_dotenv()

VPN_PATH = os.getenv('VPN_PATH')
SERVER = os.getenv('SERVER')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
DOMAIN = os.getenv('DOMAIN')

process = subprocess.Popen(VPN_PATH)
time.sleep(3)

window = pygetwindow.getWindowsWithTitle('NetExtender')[0]
window.activate()
time.sleep(2)

p.moveTo(1000, 400)
p.click()

list = [ SERVER, USER_NAME, PASSWORD, DOMAIN ]
print(list)

for data in list:
    p.keyDown('tab')
    p.hotkey('ctrl', 'a')
    p.write(data)
    time.sleep(2)

p.keyDown('enter')
