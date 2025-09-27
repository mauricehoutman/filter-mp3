import os
import glob

folder = "/raid5/music/Maurice" # Change folder path
files = glob.glob(os.path.join(folder, "**", "*"), recursive=True)

for file_path in files:
    if os.path.isfile(file_path):
        if not file_path.lower().endswith("mp3"):
            os.remove(file_path)
