#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path

def get_script_path():
    package_dir = Path(__file__).resolve().parent
    script_path = Path(package_dir, "scripts", "frugalSot.sh")
    return script_path

def main():
    parser = argparse.ArgumentParser(
        description="FrugalSOT - Optimized AI Inference for Edge Devices"
    )
    parser.add_argument(
        "prompt",
        type=str,
        help="The prompt to process"
    )
    # parser.add_argument(
    #     "--model",
    #     choices=["tiny", "small", "medium", "large"],
    #     help="Force a specific model size"
    # )
    
    args = parser.parse_args()

    script_path = get_script_path()

    os.chmod(script_path, 0o755)

    try:
        process = subprocess.Popen(
            ["bash", str(script_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=args.prompt)
        
        print(stdout)
        if stderr:
            print(f"Errors: {stderr}", file=sys.stderr)
            
    except Exception as e:
        print(f"Error running FrugalSOT: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()