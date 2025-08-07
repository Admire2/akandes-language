@echo off
REM Batch file to run workspace verification and push to GitHub
cd /d "C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace"
python verify_workspace_structure.py
git push
C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace\run_and_push.bat
