import webbrowser
import platform
import json
import time

chrome_path = ''

# MacOS
if platform.system() == 'Darwin':
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
elif platform.system() == 'Windows':
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
else:
    chrome_path = '/usr/bin/google-chrome %s'

f = open("holo.json")
vids = json.load(f)

for s in vids:
    webbrowser.get(chrome_path).open(s)
    time.sleep(2)