#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path

def get_script_path():
    # Get the directory where cli.py is located
    package_dir = Path(__file__).resolve().parent
    # Construct path to the script relative to cli.py
    script_path = package_dir / "scripts" / "frugalSot.sh"
    
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found at: {script_path}")
        
    return script_path

def main():
    print("running cli.py ....")
    parser = argparse.ArgumentParser(
        description="FrugalSOT - Optimized AI Inference for Edge Devices"
    )
    parser.add_argument(
        "prompt",
        type=str,
        help="The prompt to process"
    )
    
    args = parser.parse_args()

    script_path = Path("scripts/frugalSot.sh")
    print(f"Script path: {script_path}")
    print(f"Script exists: {Path(script_path).exists()}")
    print(f"Script is executable: {os.access(script_path, os.X_OK)}")

    # Ensure script is executable
    os.chmod(script_path, 0o755)

    try:
        print(f"Prompt: {args.prompt}")
        print("Attempting to execute script...")
        cmd = ["bash", str(script_path), args.prompt]
        print(f"Command: {' '.join(cmd)}")
        
        # Use run instead of Popen for simpler handling
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False  # Don't raise exception on non-zero return
        )
        
        print(f"Process return code: {result.returncode}")
        if result.stdout:
            print(f"Stdout: {result.stdout}")
        if result.stderr:
            print(f"Stderr: {result.stderr}", file=sys.stderr)
            
        if result.returncode != 0:
            sys.exit(result.returncode)
            
    except Exception as e:
        print(f"Error running FrugalSOT: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()