import os
import shutil

source_folder = "files"
destination_folder = "text_files"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".txt"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )

print("Text files organized successfully.")



