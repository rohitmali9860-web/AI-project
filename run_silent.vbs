' ===========================================================================
' run_silent.vbs - Launches Daily Python Practice silently in the background
' Prevents popping black command prompt windows during Task Scheduler runs
' ===========================================================================
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("WScript.Shell")

strScriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)
strBatPath = """" & strScriptDir & "\run_daily.bat"""

' Run hidden (0 = hide window, True = wait for completion)
intReturn = objShell.Run(strBatPath, 0, True)
WScript.Quit intReturn
