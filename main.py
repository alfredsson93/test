import tkinter as tk
import requests
import os
import subprocess

def check_for_updates():
    # Replace 'YOUR_GITHUB_REPO_URL' with the URL of your GitHub repository
    repo_url = 'https://api.github.com/repos/alfredsson93/test/releases/latest'
    response = requests.get(repo_url)
    if response.status_code == 200:
        latest_version = response.json()['tag_name']
        if latest_version != current_version:
            update_status.config(text="New version available!")
            download_update()
        else:
            update_status.config(text="You have the latest version.")
    else:
        update_status.config(text="Failed to check for updates.")

def download_update():
    # Replace 'YOUR_GITHUB_REPO_URL' with the URL of your GitHub repository
    exe_url = 'https://github.com/alfredsson93/test/releases/latest/download/your_script.exe'
    exe_filename = 'your_script.exe'
    try:
        update_status.config(text="Downloading update...")
        with open(exe_filename, 'wb') as f:
            response = requests.get(exe_url)
            f.write(response.content)
        update_status.config(text="Update downloaded. Restart to apply.")
    except Exception as e:
        update_status.config(text=f"Failed to download update: {str(e)}")

# Replace '2.0' with the current version of your script
current_version = '2.0'

# GUI Setup
root = tk.Tk()
root.title("OTA Update Test")

version_label = tk.Label(root, text=f"Current Version: {current_version}")
version_label.pack(pady=10)

update_button = tk.Button(root, text="Check for Updates", command=check_for_updates)
update_button.pack(pady=5)

update_status = tk.Label(root, text="")
update_status.pack(pady=5)

root.mainloop()
