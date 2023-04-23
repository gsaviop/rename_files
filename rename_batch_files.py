import os
import glob

base_name = str(input("What's the desired base name for your files? "))
print(" ")
file_path = str(input("Where's the directory your batch of files located at? "))
print(" ")
start_num = int(input("From which integer will you start numbering your files? "))

files = glob.glob(os.path.join(file_path, "*"))

for file in files:
    file_ext = os.path.splitext(file)[1]

    new_file_name = f"{base_name}{start_num}{file_ext}"

    new_path = os.path.join(file_path, new_file_name)

    os.rename(file, new_path)

    start_num += 1

print("All files renamed successfully!")

