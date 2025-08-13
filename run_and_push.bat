@echo off
REM Batch file to verify workspace and push all changes to GitHub automatically
cd /d "C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace"
python verify_workspace_structure.py
git add .
git commit -m "Auto-commit: workspace update"
git push
