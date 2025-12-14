#!/usr/bin/env python3
import zipfile
import os

INCLUDE_FILES = [
    'manifest.json',
    '__init__.py',
    'base_dialog.py',
    'browser.py',
    'tools.py',
    'config_manager.py',
    'config.json',
    'anki_util.py',
    'logger.py',
    'yomitan_api.py',
]

INCLUDE_DIRS = [
    'user_files',
]

EXCLUDE_PATTERNS = [
    '__pycache__',
    '.pyc',
    '.pyo',
    '.DS_Store',
    '.git',
    '.gitignore',
    '.idea',
    '.claude',
    'screenshot',
    'README.md',
    '.pytest_cache',
    'build_addon.py',
]

def should_exclude(path):
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path:
            return True
    return False

def create_addon_zip():
    addon_dir = os.path.basename(os.getcwd())
    zip_filename = f"{addon_dir}.ankiaddon"

    print(f"Creating addon package: {zip_filename}")
    print("-" * 50)

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in INCLUDE_FILES:
            if os.path.exists(filename):
                print(f"Adding: {filename}")
                zipf.write(filename)
            else:
                print(f"Warning: {filename} not found, skipping")

        for dirname in INCLUDE_DIRS:
            if os.path.exists(dirname):
                for root, dirs, files in os.walk(dirname):
                    dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
                    for file in files:
                        filepath = os.path.join(root, file)
                        if not should_exclude(filepath):
                            print(f"Adding: {filepath}")
                            zipf.write(filepath)
            else:
                print(f"Warning: {dirname} directory not found, skipping")

    print("-" * 50)
    print(f"✓ Addon package created: {zip_filename}")
    print(f"✓ File size: {os.path.getsize(zip_filename):,} bytes")
    print()
    print("Installation instructions:")
    print("1. Open Anki")
    print("2. Go to Tools → Add-ons")
    print("3. Click 'Install from file...'")
    print(f"4. Select: {zip_filename}")
    print("5. Restart Anki")

    return zip_filename

if __name__ == '__main__':
    create_addon_zip()
