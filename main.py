import time
import requests
import platform
import datetime
import os
import sys
import psutil

WEBHOOK_URL = "YOUR_WEBHOOK_HERE"

# Safe folder (change if you want)
TARGET_FOLDER = os.path.expanduser("~/Downloads")

def get_system_info():
    return {
        "OS": platform.system() + " " + platform.release(),
        "CPU": platform.processor() or "Unknown",
        "Machine": platform.machine(),
        "Python": sys.version.split()[0],
        "RAM_GB": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }

def get_folder_count(path):
    try:
        return len(os.listdir(path))
    except:
        return "Unavailable"

def send_embed():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sys_info = get_system_info()
    folder_count = get_folder_count(TARGET_FOLDER)

    embed = {
        "title": "System Dashboard",
        "color": 3447003,  # blue
        "fields": [
            {"name": " Time Ran", "value": now, "inline": False},
            {"name": " OS", "value": sys_info["OS"], "inline": True},
            {"name": " CPU", "value": sys_info["CPU"], "inline": True},
            {"name": " Machine", "value": sys_info["Machine"], "inline": True},
            {"name": " Python", "value": sys_info["Python"], "inline": True},
            {"name": "RAM (GB)", "value": str(sys_info["RAM_GB"]), "inline": True},
            {"name": "Downloads Files", "value": str(folder_count), "inline": True}
        ],
        "footer": {
            "text": "Safe Info"
        }
    }

    data = {
        "username": "System Bot",
        "embeds": [embed]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        print("Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

send_embed()

while True:
    print("Running safely...")
    time.sleep(5)