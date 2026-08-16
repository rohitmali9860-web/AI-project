@echo off
REM ===========================================================================
REM Daily Python Practice - Manual & Task Runner
REM ===========================================================================
cd /d "%~dp0"

echo [Daily Python Practice] Starting automation script...
python "%~dp0daily_practice.py" %*

set EXITCODE=%ERRORLEVEL%
if %EXITCODE% EQU 0 (
    echo [Daily Python Practice] Run finished successfully.
) else (
    echo [Daily Python Practice] Run finished with exit code %EXITCODE%. Check practice-log.txt.
)

REM If double-clicked directly in Windows Explorer, pause so the user can see output
if "%1"=="" (
    if "%CMDCMDLINE%" == "%COMSPEC% /c %0 " pause
)

exit /b %EXITCODE%
