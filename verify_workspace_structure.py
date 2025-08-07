import os
import datetime
import subprocess

# Main workspace to check
main_workspace = r"C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace"

# Key folders and files to verify (add or adjust as needed)
key_folders = [
    "akandes_docs",
    "akandes_python_backend",
    "hdl_projects",
    "src",
    ".github"
]
key_files = [
    ".chips",
    "README.md",
    "AKANDECHIPS_LANGUAGE_DOCUMENTATION.md",
    "AKANDECHIPS_LANGUAGE_DOCUMENTATION2.md"
]

missing = []
created = []
log_lines = []

def log(msg):
    print(msg)
    log_lines.append(msg)


log("Verifying key folders:")
for folder in key_folders:
    folder_path = os.path.join(main_workspace, folder)
    if not os.path.isdir(folder_path):
        log(f"[MISSING] {folder_path}")
        try:
            os.makedirs(folder_path)
            log(f"[CREATED] {folder_path}")
            created.append(folder_path)
        except Exception as e:
            log(f"[ERROR] Could not create {folder_path}: {e}")
        missing.append(folder_path)
    else:
        log(f"[OK]      {folder_path}")


log("\nVerifying key files:")
for file in key_files:
    file_path = os.path.join(main_workspace, file)
    if not os.path.isfile(file_path):
        log(f"[MISSING] {file_path}")
        try:
            # Create placeholder file if missing
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# Placeholder for {file}\n")
            log(f"[CREATED] {file_path}")
            created.append(file_path)
        except Exception as e:
            log(f"[ERROR] Could not create {file_path}: {e}")
        missing.append(file_path)
    else:
        log(f"[OK]      {file_path}")


if missing:
    log("\nSome key files or folders were missing and have been created if possible. Please review the list above.")
else:
    log("\nAll key files and folders are present.")

# Log results to a file
log_file = os.path.join(main_workspace, "workspace_verification_log.txt")
with open(log_file, "a", encoding="utf-8") as lf:
    lf.write(f"\n--- Verification run at {datetime.datetime.now()} ---\n")
    for line in log_lines:
        lf.write(line + "\n")

# Git integration: auto-stage and commit created items if git is present
def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

if created and is_git_repo(main_workspace):
    try:
        # Stage new files/folders
        subprocess.run(["git", "add"] + created, cwd=main_workspace, check=True)
        # Commit
        commit_msg = f"Auto-created missing workspace items on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=main_workspace, check=True)
        log(f"\n[Git] Auto-staged and committed created items.")
    except Exception as e:
        log(f"\n[Git ERROR] Could not auto-commit: {e}")
elif created:
    log("\n[Git] Not a git repository. Skipped auto-commit.")

# Scheduling note
log("\nTo schedule this script to run automatically, use Windows Task Scheduler. (See script comments for guidance.)")
