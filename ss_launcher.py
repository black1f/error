#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# استيراد الملف المترجم
try:
    import ss as module
    if __name__ == "__main__":
        if hasattr(module, 'main'):
            module.main()
        else:
            print("Module loaded successfully")
except Exception as e:
    print(f"Error loading module: {e}")
    sys.exit(1)
