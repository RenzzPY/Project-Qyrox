#!/usr/bin/env python3
"""
Qyrox V4.6 - Official Installer
Install via: python -c "$(curl -fsSL https://raw.githubusercontent.com/[your-username]/qyrox/main/install.py)"
"""

import os
import sys
import urllib.request
import zipfile
import tempfile
from pathlib import Path

QYROX_VERSION = "4.6.0"
DOWNLOAD_URL = "https://github.com/[your-username]/qyrox/releases/download/v4.6.0/qyrox-v4.6-source.zip"

def install():
    print("=" * 60)
    print("  Qyrox V4.6 - Official Installer")
    print("=" * 60)
    print()
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("[ERROR] Python 3.8+ required")
        sys.exit(1)
    
    print("[OK] Python version OK")
    
    # Download
    print(f"\nDownloading Qyrox V{QYROX_VERSION}...")
    temp_dir = tempfile.mkdtemp()
    zip_path = Path(temp_dir) / "qyrox.zip"
    
    try:
        urllib.request.urlretrieve(DOWNLOAD_URL, zip_path)
        print("[OK] Download complete")
    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        sys.exit(1)
    
    # Extract
    print("\nExtracting files...")
    install_dir = Path.home() / "qyrox"
    install_dir.mkdir(exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(install_dir)
    
    print(f"[OK] Installed to: {install_dir}")
    
    # Install dependencies
    print("\nInstalling dependencies...")
    os.system(f"pip install -r {install_dir}/requirements.txt")
    
    # Run setup
    print("\nRunning setup wizard...")
    os.chdir(install_dir)
    os.system("python setup.py")
    
    print("\n" + "=" * 60)
    print("  Installation Complete!")
    print("=" * 60)
    print(f"\nTo start Qyrox:")
    print(f"  cd {install_dir}")
    print(f"  python main.py")
    print()

if __name__ == "__main__":
    try:
        install()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nInstallation failed: {e}")
        sys.exit(1)
