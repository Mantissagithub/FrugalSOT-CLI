# import subprocess
import json
# from dotenv import load_dotenv
import os
from pathlib import Path

from prompt import classify_prompt_complexity

# load_dotenv()
# REMOTE_PATH = os.getenv('REMOTE_PATH')

import sys

# prompt = "what is AI?"
if len(sys.argv) < 2:
    print("Please provide a prompt as an argument.")
    sys.exit(1)

prompt = sys.argv[1]
complexity = classify_prompt_complexity(prompt)

test_path = Path("data/test.txt")


with open(test_path, "w") as f:
    f.write(str(json.dumps({"prompt":prompt,"complexity":complexity})))

# command = ["scp", "data/test.txt", REMOTE_PATH]
# subprocess.run(command, check=True)