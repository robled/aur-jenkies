#!/usr/bin/env python3

import sys
import requests

try:
    sys.argv[1]
except IndexError:
    print("Usage: " + sys.argv[0] + " <username>")
    sys.exit(1)

r = requests.get("https://aur.archlinux.org/rpc/?v=5&type=search&by=maintainer&arg=" + sys.argv[1])

if not r.json()["results"]:
        print("Error: no results returned. Verify username is correct.")
        sys.exit(1)

with open("packages.yaml.inc", "w") as f:
    for result in r.json()["results"]:
        print("Writing \"" + result["Name"] + "\" to packages.yaml.inc")
        f.write("- " + result["Name"] + "\n")
    f.close()
