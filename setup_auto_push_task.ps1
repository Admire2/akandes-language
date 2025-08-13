# PowerShell script to set up Windows Task Scheduler for auto git push
# 1. Runs run_and_push.bat every 30 minutes
# 2. Runs run_and_push.bat at system startup

$taskName = "AkandesAutoPush"
$scriptPath = "C:\Users\great\OneDrive\Documents\AKANDES_LANGUAGE_INSTALLER\workspace\workspace3\workspace\run_and_push.bat"

# Remove existing task if present
if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Set start time to now + 1 minute
$startTime = (Get-Date).AddMinutes(1)
# Set repetition duration to 7 days
$repetitionDuration = New-TimeSpan -Days 7

# Create trigger: every 30 minutes, for 7 days
$trigger1 = New-ScheduledTaskTrigger -Once -At $startTime -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration $repetitionDuration
# Create trigger: at logon
$trigger2 = New-ScheduledTaskTrigger -AtLogOn

# Create action
$action = New-ScheduledTaskAction -Execute $scriptPath

# Register the task
Register-ScheduledTask -TaskName $taskName -Trigger $trigger1, $trigger2 -Action $action -RunLevel Highest -Force

Write-Host "Auto-push task scheduled: every 30 minutes (for 7 days) and at system startup."
