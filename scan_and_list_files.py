import os

base_dir = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        print(os.path.join(root, file))
        