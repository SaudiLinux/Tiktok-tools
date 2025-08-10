#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for TikTok Tools installation
Author: SayerLinux
"""

import sys
import os
import subprocess

def check_python():
    """Check Python installation"""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 6:
            print("✅ Python version:", sys.version.split()[0])
            return True
        else:
            print("❌ Python 3.6+ required, found:", sys.version.split()[0])
            return False
    except Exception as e:
        print("❌ Error checking Python:", str(e))
        return False

def check_dependencies():
    """Check required dependencies"""
    required_packages = [
        'requests',
        'beautifulsoup4',
        'lxml',
        'colorama',
        'urllib3'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_files():
    """Check if all required files exist"""
    required_files = [
        'tiktok-tools.py',
        'requirements.txt',
        'README.md',
        'INSTALL.md',
        'config.py'
    ]
    
    missing = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing.append(file)
    
    return len(missing) == 0, missing

def install_missing_packages(missing):
    """Install missing packages"""
    if missing:
        print(f"\n📦 Installing missing packages: {', '.join(missing)}")
        for package in missing:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    return True

def main():
    """Main verification function"""
    print("🔍 TikTok Tools - Installation Verification")
    print("=" * 50)
    
    # Check Python
    print("\n1. Checking Python...")
    python_ok = check_python()
    
    # Check dependencies
    print("\n2. Checking dependencies...")
    deps_ok, missing_deps = check_dependencies()
    
    # Check files
    print("\n3. Checking files...")
    files_ok, missing_files = check_files()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY:")
    
    if python_ok and deps_ok and files_ok:
        print("🎉 All checks passed! TikTok Tools is ready to use.")
        print("\n💡 To start using the tool:")
        print("   Run: python tiktok-tools.py")
        print("   Or:  python tiktok-tools.py username")
    else:
        print("⚠️  Some issues found:")
        
        if not python_ok:
            print("   - Python version issue")
        
        if missing_deps:
            print(f"   - Missing packages: {', '.join(missing_deps)}")
            install = input("\n🤔 Install missing packages? (y/n): ").lower().strip()
            if install == 'y':
                install_missing_packages(missing_deps)
        
        if missing_files:
            print(f"   - Missing files: {', '.join(missing_files)}")
            print("   - Please re-download the complete package")

if __name__ == "__main__":
    main()