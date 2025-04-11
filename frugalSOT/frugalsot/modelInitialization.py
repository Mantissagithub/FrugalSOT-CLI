import json
import sys
import os
from pathlib import Path

def modelsInitialization(ramGB):
    # print("Running modelsInitialization.py...")
    # print(f"RAM Size: {ramGB} GB")
    config_path = Path("data/config.json")
    with open(str(config_path), 'r') as f:
        data = json.load(f)
    
    config = data["MoreThan8GB"] if ramGB >= 8 else data["LessThan8gb"]
    
    print(json.dumps(config))
    # return json.dumps(config)

if __name__ == "__main__":
    ramGB = float(sys.argv[1])
    modelsInitialization(ramGB)
