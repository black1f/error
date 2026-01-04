#!/usr/bin/env python3
import os
import sys

# Add the 'so' folder to python path
# This works even if the tool is moved
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'so'))

def banner():
    print("""
    [1;32m╔══════════════════════════════════════════════════════════════╗
    ║  [1;37mALI - PROFESSIONAL TOOL[1;32m                       ║
    ║  [1;37mStatus: [1;32mEncrypted & Protected[1;32m                       ║
    ╚══════════════════════════════════════════════════════════════╝[0m
    """)

def main():
    banner()
    try:
        import core_logic
        if hasattr(core_logic, 'main'): core_logic.main()
        elif hasattr(core_logic, 'run'): core_logic.run()
    except ImportError as e:
        print(f"\n[1;31m[!] Error: Core component missing in 'so' folder![0m")
        print(f"Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
