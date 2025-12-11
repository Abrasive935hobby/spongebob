"""Test runner for W0522168alarm-deactivation-final.py/code.py

Usage (PowerShell):
    python .\run_test.py

This runner will simulate entering the first password from
`W0522168alarm-deactivation-final.py/passwords.txt` twice (activate then deactivate).
"""
import builtins
import importlib.util
import os
import sys

# Build path to target module
repo_root = os.path.dirname(__file__)
module_dir = os.path.join(repo_root, "W0522168alarm-deactivation-final.py")
module_path = os.path.join(module_dir, "code.py")
passwords_path = os.path.join(module_dir, "passwords.txt")

# Read first password to use for activate/deactivate
try:
    with open(passwords_path, "r", encoding="utf-8") as f:
        pw = f.readline().strip()
        if not pw:
            print("No passwords found in passwords.txt")
            sys.exit(1)
except FileNotFoundError:
    print(f"passwords.txt not found at {passwords_path}")
    sys.exit(1)

# Prepare simulated inputs (activate then deactivate)
inputs = [pw, pw]

def input_mock(prompt=""):
    # mimic built-in input by printing the prompt and returning next value
    print(prompt, end="")
    try:
        return inputs.pop(0)
    except IndexError:
        raise EOFError("No more input")

builtins.input = input_mock

# Load module from path and run main()
spec = importlib.util.spec_from_file_location("alarm_code", module_path)
if spec is None:
    print(f"Could not find module at {module_path}")
    sys.exit(1)
module = importlib.util.module_from_spec(spec)
loader = spec.loader
if loader is None:
    print("Module loader missing")
    sys.exit(1)

try:
    loader.exec_module(module)
except Exception:
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Call main if present
if hasattr(module, "main"):
    module.main()
else:
    print("module has no main()")
