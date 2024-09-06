
# connect-vpn

Service created to auto connect in VPN app called NetExtender, software from @SonicWall

**Python version :** ^3.2

## Installation

To start service is necessary to create `.env` file.

Install dependencies
```bash
  pip install -r requirements.txt
```

Start scrypt
```bash
  python script.py
```
If the reconnect button appears, press it and stop moving the mouse.


## Generating a .exe

```bash
  pyinstaller --onefile --add-data ".env;." script.py  
```
It will generate a .exe in the folder /dist

This exe not run out of this folder because dependencies and .env file but you can to create a shortcut this exe.