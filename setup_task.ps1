# ===========================================================================
# setup_task.ps1 - Registers Windows Scheduled Task for Daily Python Practice
# ===========================================================================

$TaskName = "DailyPythonPractice"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VbsPath = Join-Path $ScriptDir "run_silent.vbs"
$BatPath = Join-Path $ScriptDir "run_daily.bat"

Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host "   Registering Daily Python Practice Scheduled Task       " -ForegroundColor Cyan
Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host "Task Name:        $TaskName"
Write-Host "Schedule:         Daily at 09:00 AM"
Write-Host "Catch-Up Option:  Enabled (Start as soon as possible if missed)"
Write-Host "Runner Script:    $VbsPath"
Write-Host "Target Directory: $ScriptDir"
Write-Host "-----------------------------------------------------------"

# Check if script files exist
if (-not (Test-Path $VbsPath)) {
    Write-Error "Could not find $VbsPath! Please ensure the file exists."
    exit 1
}

# 1. Define Action: Execute VBScript runner invisibly via wscript.exe
$Action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "`"$VbsPath`"" -WorkingDirectory "$ScriptDir"

# 2. Define Trigger: Daily at 9:00 AM
$Trigger = New-ScheduledTaskTrigger -Daily -At "09:00AM"

# 3. Define Settings: Catch up if missed, allow battery run, ignore overlaps
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15) `
    -MultipleInstances IgnoreNew

# 4. Define Principal: Current User Interactive Logon (Preserves Git Credential Manager and SSH Keys)
$CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$Principal = New-ScheduledTaskPrincipal -UserId $CurrentUser -LogonType Interactive

# 5. Check if task already exists and unregister cleanly
$ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($ExistingTask) {
    Write-Host "Found existing task '$TaskName'. Replacing with updated settings..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# 6. Register Task
try {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $Action `
        -Trigger $Trigger `
        -Settings $Settings `
        -Principal $Principal `
        -Description "Automated Daily Python Practice challenge generator and GitHub committer." | Out-Null

    Write-Host "`n[SUCCESS] Scheduled Task '$TaskName' registered successfully!" -ForegroundColor Green
    Write-Host "The task will trigger daily at 9:00 AM. If your PC is off, it will catch up on next login." -ForegroundColor Green
} catch {
    Write-Error "Failed to register scheduled task: $_"
    exit 1
}

Write-Host "`n-----------------------------------------------------------"
Write-Host "Commands to manage your task:" -ForegroundColor Cyan
Write-Host "  - Test run task immediately:  Start-ScheduledTask -TaskName `"$TaskName`""
Write-Host "  - Check task status:          Get-ScheduledTask -TaskName `"$TaskName`""
Write-Host "  - Remove scheduled task:      Unregister-ScheduledTask -TaskName `"$TaskName`""
Write-Host "===========================================================`n"
