import os
import shutil

# Set your main workspace directory
main_workspace = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace"

# Set the parent directory containing all workspaces
parent_dir = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace"

# Folders to skip (don't move from or into these)
skip_folders = [
    "workspace3",  # Don't move from the main workspace
    "node_modules", "out", ".git", ".github", "snippets", "syntaxes", "vs-code-recorder"
]

def should_skip(path):
    for skip in skip_folders:
        if skip in path:
            return True
    return False

for root, dirs, files in os.walk(parent_dir):
    # Skip the main workspace and unwanted folders
    if should_skip(root):
        continue
    for file in files:
        src_path = os.path.join(root, file)
        # Compute relative path from parent_dir
        rel_path = os.path.relpath(src_path, parent_dir)
        dest_path = os.path.join(main_workspace, rel_path)
        dest_folder = os.path.dirname(dest_path)
        # Only move if not already in main workspace
        if not src_path.startswith(main_workspace):
            os.makedirs(dest_folder, exist_ok=True)
            # If file exists at destination, rename source to avoid overwrite
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(dest_path)
                dest_path = f"{base}_from_old{ext}"
            print(f"Moving {src_path} -> {dest_path}")
            shutil.move(src_path, dest_path)

print("Migration complete. Please review your main workspace for all files.")