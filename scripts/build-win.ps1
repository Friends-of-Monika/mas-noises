#!/bin/pwsh

# This script creates a .zip package with your submod files.
# Below you can configure some of its parameters, but generally,
# unless you know what you're doing, DO NOT change actual code.


# CLI -Header parameter declaration
param ([string] $Header)


# Whether to create enclosing submod folder or not (usually you'd keep it $true)
$CreateSubmodFolder = $true

# Prefix to prepend to the submod folder. When packaging a submod that adds
# something in the game/ folder, it is better to set this to "game/Submods"
$PrefixPath = "Submods"

# Format string for the file name of your submod .zip file. The following
# placeholders are used:
#   {0} - submod name in lowercase, spaces replaced with -
#   {1} - submod version in lowercase, spaces replaced with -
$ZipFileFormat = "{0}-{1}.zip"

# Various folders in the project layout, only change if you moved any of the
# folders listed here anywhere or renamed them.
$ProjectScriptsDir = "scripts"
$ProjectBuildDir = "build"
$ProjectModDir = "mod"
$ProjectLibDir = "lib"
$ProjectResDir = "res"


# Locate script file location and create temp directory
$Dir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Definition)
$Temp = (New-Item -ItemType Directory -Path `
    (Join-Path ([System.IO.Path]::GetTempPath()) `
    ([System.IO.Path]::GetRandomFileName())))

if (-not $Header) {
    # Locate header files automatically and parse JSON
    $Headers = python "$Dir/$ProjectScriptsDir/find_header.py" find `
        "$Dir/$ProjectModDir" | ConvertFrom-Json

    # No idea why do we have to go through such hoops, but
    # otherwise it's not working too well with JSON objects
    $HeaderPaths = $Headers `
        | Get-Member -MemberType NoteProperty `
        | Select-Object -ExpandProperty Name

    # Check that we have at least some of them
    if ($HeaderPaths.count -eq 0) {
        Write-Error "Cannot build submod! Found no valid header files."
        Exit 2

    # But not more than one, so we can't choose
    } elseif ($HeaderPaths.count -gt 1) {
        Write-Error "Cannot build submod! Found too many valid header files."
        Write-Error "Run this script with -Header parameter instead."
        Exit 2
    }

    # Save header values to $Submod
    Write-Output "Found valid submod header in $($HeaderPaths `
        | Resolve-Path -Relative)!"
    $Submod = $Headers | Select-Object -ExpandProperty "$HeaderPaths"

} else {
    # Parse header from the provided header .rpy script and parse JSON
    $Submod = python "$Dir/$ProjectScriptsDir/find_header.py" header "$Header" `
        2> $null | ConvertFrom-Json

    # File may be an invalid header, so handle this
    if ($LastExitCode -ne 0) {
        Write-Error "Invalid header file: $Header!"
        Exit 2
    }

    Write-Output "Using provided submod header in $($Header)."
}


# Create build directory
$Build = "$Dir\$ProjectBuildDir"
New-Item -ItemType Directory -Force -Path "$Build" > $null

# {0} variable in $ZipFileFormat
$Name = $Submod.Name.ToLower() -Replace "\s", "-"
# {1} variable in $ZipFileFormat
$Version = $Submod.Version.ToLower() -Replace "\s", "-"
# Package file name
$Package = $ZipFileFormat -f "$Name", "$Version"


Write-Output "Packaging $($Submod.Name) $($Submod.Version)..."
Write-Output "Created .zip will be saved as $ProjectBuildDir\$Package."

# Create mod folder with prefix
$Mod = "$Temp\$PrefixPath"
if ($CreateSubmodFolder) { $Mod = "$Mod\$($Submod.Name)" }
#New-Item -ItemType Directory -Force -Path "$Mod" > $null

# Copy mod files, optionally copy lib/
Copy-Item -Recurse "$Dir\$ProjectModDir" "$Mod"
if (Test-Path -Path "$Dir\$ProjectLibDir") {
    Copy-Item -Recurse "$Dir\$ProjectLibDir" "$Mod" }

if (Test-Path -Path "$Dir\$ProjectResDir") {
    Copy-Item -Recurse "$Dir\$ProjectResDir" "$Mod" }

# Remove .gitkeep and README.md
Get-ChildItem -Path $Temp -Recurse -Include ".gitkeep", "README.md" `
    | Remove-Item -Force

# Create .zip, remove temp folder
$PackageRoot = Get-ChildItem -Path "$Temp" -Directory `
    | Select-Object -First 1
Compress-Archive -Update -Path "$PackageRoot" -DestinationPath "$Build\$Package"
Remove-Item -Force -Recurse "$Temp"