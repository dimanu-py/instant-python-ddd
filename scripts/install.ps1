# Install the latest instant-python (ipy) release binary for Windows.
#
# Usage:
#
#   powershell -ExecutionPolicy ByPass -c "irm https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.ps1 | iex"
#
# Overridable via env vars:
#   IPY_BIN_DIR   install destination directory (default: $env:USERPROFILE\.local\bin)

$ErrorActionPreference = "Stop"

$Repo = "dimanu-py/instant-python"
$Target = "x86_64-pc-windows-msvc"
$BinDir = if ($env:IPY_BIN_DIR) { $env:IPY_BIN_DIR } else { Join-Path $env:USERPROFILE ".local\bin" }
$Dest = Join-Path $BinDir "ipy.exe"

# --- confirm the current machine matches our only prebuilt target -----------
function Confirm-SupportedArchitecture {
    $arch = $env:PROCESSOR_ARCHITECTURE
    if ($arch -ne "AMD64") {
        Write-Error "ipy: no prebuilt binary for Windows-$arch. Install via 'uv tool install instant-python' or pipx/pip instead - see https://dimanu-py.github.io/instant-python/getting_started/installation/"
        exit 1
    }
}

# --- download the matching release asset -------------------------------------
function Get-Binary {
    param([string]$Destination)

    $url = "https://github.com/$Repo/releases/latest/download/ipy-${Target}.exe"
    Write-Host "ipy: downloading latest release for $Target ..."
    Invoke-WebRequest -Uri $url -OutFile $Destination -UseBasicParsing
}

# --- move the binary into place ------------------------------------------------
function Install-Binary {
    param([string]$Source)

    Write-Host "ipy: installing to $Dest ..."
    New-Item -ItemType Directory -Force -Path $BinDir | Out-Null
    Move-Item -Force -Path $Source -Destination $Dest
}

# Persist the install dir on the user's PATH so `ipy` works in new terminals.
function Add-InstallDirToPath {
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $pathEntries = $userPath -split ";" | Where-Object { $_ -ne "" }

    if ($pathEntries -notcontains $BinDir) {
        $newPath = if ($userPath) { "$userPath;$BinDir" } else { $BinDir }
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Host "ipy: added $BinDir to your user PATH. Restart your terminal to pick it up."
    }

    if (($env:Path -split ";") -notcontains $BinDir) {
        $env:Path = "$env:Path;$BinDir"
    }
}

function Confirm-Installation {
    & $Dest --version
}

function Main {
    Confirm-SupportedArchitecture

    $tmp = Join-Path ([System.IO.Path]::GetTempPath()) ([System.IO.Path]::GetRandomFileName())
    New-Item -ItemType Directory -Force -Path $tmp | Out-Null
    try {
        $download = Join-Path $tmp "ipy.exe"
        Get-Binary -Destination $download
        Install-Binary -Source $download
        Add-InstallDirToPath
        Confirm-Installation
    }
    finally {
        Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
    }
}

Main
