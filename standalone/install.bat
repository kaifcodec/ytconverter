@echo off
cd /d "%~dp0"
setlocal enabledelayedexpansion

echo -------------------------------
echo YTConverter Windows Installer
echo -------------------------------

:: ---------------- Paths ----------------
set "TEMP_DIR=%cd%\installer_temp"
set "TOOLS_DIR=%LocalAppData%\Programs\YTConverter"
set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
set "FFMPEG_ZIP=%TEMP_DIR%\ffmpeg.zip"
set "FFMPEG_BIN_DIR="

echo Creating temporary folder...
mkdir "%TEMP_DIR%" >nul 2>&1
mkdir "%TOOLS_DIR%" >nul 2>&1

:: ---------------- Check Python ----------------
echo Checking Python...
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Install it from https://www.python.org/downloads/
    exit /b 1
)
echo Python found.

:: ---------------- Install yt-dlp ----------------
echo Installing yt-dlp...
python -m pip install -U yt-dlp
if errorlevel 1 (
    echo ERROR: Failed to install yt-dlp.
    exit /b 1
)
echo yt-dlp installed successfully.

:: ---------------- Install FFmpeg ----------------
echo Checking ffmpeg...
where ffmpeg >nul 2>&1
if %errorlevel%==0 (
    echo ffmpeg already installed in system PATH.
) else (
    echo ffmpeg not found. Downloading...
    powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"
    if errorlevel 1 (
        echo ERROR: Failed to download FFmpeg.
        exit /b 1
    )

    echo Extracting FFmpeg...
    powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%TEMP_DIR%' -Force"
    if errorlevel 1 (
        echo ERROR: Failed to extract FFmpeg.
        exit /b 1
    )

    echo Searching for ffmpeg.exe...
    set "FFMPEG_BIN_DIR="
    for /r "%TEMP_DIR%" %%I in (ffmpeg.exe) do (
        set "FFMPEG_BIN_DIR=%%~dpI"
        goto :found_ffmpeg
    )
    :found_ffmpeg
    if not defined FFMPEG_BIN_DIR (
        echo ERROR: ffmpeg.exe not found after extraction
        exit /b 1
    )
    echo ffmpeg.exe found at: %FFMPEG_BIN_DIR%

    echo Copying FFmpeg to tools folder...
    xcopy /E /I /Y "%FFMPEG_BIN_DIR%" "%TOOLS_DIR%\ffmpeg"
    if errorlevel 1 (
        echo ERROR: Failed to copy FFmpeg to %TOOLS_DIR%\ffmpeg
        exit /b 1
    )
    echo FFmpeg installed successfully.
)

:: ---------------- Update PATH ----------------
echo Updating user PATH...
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "OLD_PATH=%%b"
if not defined OLD_PATH set "OLD_PATH=%PATH%"
setx PATH "%TOOLS_DIR%\ffmpeg;%OLD_PATH%"
echo PATH updated. Please open a new Command Prompt to use ffmpeg and yt-dlp.

:: ---------------- Cleanup ----------------
echo Cleaning up temporary files...
rmdir /S /Q "%TEMP_DIR%" >nul 2>&1

echo -------------------------------
echo Installation complete.
echo You can now run:
echo yt-dlp --version
echo ffmpeg -version
pause
exit /b 0
