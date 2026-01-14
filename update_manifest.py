# update_manifest.py
import os
import json

# Configuration
AUDIO_EXTENSIONS = {'.mp3', '.m4a', '.wav'}
OUTPUT_FILE = 'music.json'

def main():
    files = []
    # 1. Scan current directory
    for f in os.listdir('.'):
        if os.path.isfile(f):
            ext = os.path.splitext(f)[1].lower()
            if ext in AUDIO_EXTENSIONS:
                files.append({'filename': f})

    # 2. Sort by filename to prevent random git diffs
    files.sort(key=lambda x: x['filename'])

    # 3. Write Manifest
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(files, f, indent=2)
    
    print(f"🎵 Manifest updated: {len(files)} tracks found.")

if __name__ == "__main__":
    main()
