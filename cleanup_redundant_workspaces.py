import os
import shutil

# Main workspace to keep
main_workspace = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace"

# Parent directory containing all workspaces
parent_dir = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace"

# Folders to keep (relative to parent_dir)
keep_folders = [
    "workspace3",  # main workspace
    "node_modules", "out", ".git", ".github", "snippets", "syntaxes", "vs-code-recorder"
]

for item in os.listdir(parent_dir):
    item_path = os.path.join(parent_dir, item)
    # Skip files and folders to keep
    if item in keep_folders or item == os.path.basename(main_workspace):
        continue
    # Remove directories
    if os.path.isdir(item_path):
        print(f"Deleting folder: {item_path}")
        shutil.rmtree(item_path)
    # Remove files at the root of parent_dir (if any)
    elif os.path.isfile(item_path):
        print(f"Deleting file: {item_path}")
        os.remove(item_path)

print("Cleanup complete. Only the main workspace and essential folders remain.")

print("Current main workspace structure:")
for root, dirs, files in os.walk(main_workspace):
    level = root.replace(main_workspace, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")