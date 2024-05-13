# ATAC Made by Polokalap https://github.com/Polokalap https://buymeacoffee.com/Polokalap

import os
import requests
import hashlib

url = ""

data = {
    "content": f'Scanned system results - {os.getlogin()}',
    "username": "ATAC System Scan"
}

cheats = [
    "",
    "",
    "",
    "",
    ""
]

found = []


def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def scan(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_extension = os.path.splitext(file_path)[1]
                    if file_extension.lower() not in ['.exe', '.dll', '.sys']:
                        try:
                            file_hash = get_file_hash(file_path)
                            print(f'Checking the file {file_path} with the hash {file_hash}')

                            if file_hash in cheats:
                                print(f'Found {file_path}')
                                found.append(file_path)
                                found.append(file_hash)
                        except PermissionError as e:
                            print(f"Permission denied for {file_path}: {e}")
    except PermissionError as e:
        print(f"Permission denied for {directory}: {e}")


directory_to_scan = r'C:\\'
scan(directory_to_scan)

data["embeds"] = [
    {
        "description": f'Cheat hashes: {found},',
        "title": f'ATAC Results - {os.getlogin()}',
        "footer": {
            "text": "ATAC"
        }
    }
]

try:
    result = requests.post(url, json=data)
    result.raise_for_status()
except Exception as e:
    print(f"Error sending message: {e}")
