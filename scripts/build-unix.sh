#!/bin/bash

# This script creates a .zip package with your submod files.
# Below you can configure some of its parameters, but generally,
# unless you know what you're doing, DO NOT change actual code.


# CLI -header parameter
while [ "$#" -gt 0 ]; do
    case "$1" in
        -h|--header)
            shift
            Header="$1"
            break
        ;;
    esac
done

# Whether to create enclosing submod folder or not (usually you'd keep it true)
CreateSubmodFolder=true

# Prefix to prepend to the submod folder. When packaging a submod that adds
# something in the game/ folder, it is better to set this to "game/Submods"
PrefixPath="Submods"

# Format string for the file name of your submod .zip file.
ZipFileFormat="%s-%s.zip"

# Various folders in the project layout, only change if you moved any of the
# folders listed here anywhere or renamed them.
ProjectScriptsDir="scripts"
ProjectBuildDir="build"
ProjectModDir="mod"
ProjectLibDir="lib"
ProjectResDir="res"


# Locate script file location and create temp directory
Dir="$(CDPATH="" cd -- "$(dirname -- "$0")" && pwd)"
Temp="$(mktemp -d)"

if [ -z "$Header" ]; then
    # Locate header files automatically and parse JSON
    Headers="$(python "$Dir/../$ProjectScriptsDir/find_header.py" find \
        "$Dir/../$ProjectModDir" | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]')"

    # Check that we have at least some of them
    if [ -z "$Headers" ]; then
        echo "Cannot build submod! Found no valid header files."
        exit 2
    fi

    # But not more than one, so we can't choose
    HeaderCount="$(echo "$Headers" | wc -l)"
    if [ "$HeaderCount" -gt 1 ]; then
        echo "Cannot build submod! Found too many valid header files."
        echo "Run this script with --header parameter instead."
        exit 2
    fi

    # Save header values to Submod
    HeaderPath="$(echo "$Headers" | cut -d'=' -f1)"
    echo "Found valid submod header in $HeaderPath!"
    SubmodName="$(echo "$Headers" | cut -d'=' -f2- | jq -r '.name')"
    SubmodVersion="$(echo "$Headers" | cut -d'=' -f2- | jq -r '.version')"

else
    # Parse header from the provided header .rpy script and parse JSON
    if ! Submod="$(python "$Dir/$ProjectScriptsDir/find_header.py" header "$Header" \
        2> /dev/null | jq -r '.')";
    then
        echo "Invalid header file: $Header!"
        exit 2
    fi

    echo "Using provided submod header in $Header."
    SubmodName="$(echo "$Submod" | jq -r '.name')"
    SubmodVersion="$(echo "$Submod" | jq -r '.version')"
fi

# Create build directory
Build="$Dir/../$ProjectBuildDir"
mkdir -p "$Build"

# Variables in ZipFileFormat
Name="$(echo "$SubmodName" | tr '[:upper:]' '[:lower:]' | tr -s ' ' '-')"
Version="$(echo "$SubmodVersion" | tr '[:upper:]' '[:lower:]' | tr -s ' ' '-')"
# Package file name
# shellcheck disable=SC2059
Package=$(printf "$ZipFileFormat" "$Name" "$Version")

echo "Packaging $SubmodName $SubmodVersion..."
echo "Created .zip will be saved as $ProjectBuildDir/$Package."

# Create mod folder with prefix
Mod="$Temp/$PrefixPath"
if [ "$CreateSubmodFolder" = "true" ]; then Mod="$Mod/$SubmodName"; fi
mkdir -p "$Mod"

# Copy mod files, optionally copy lib/
cp -r "$Dir/../$ProjectModDir/"* "$Mod"

if [ -d "$Dir/../$ProjectLibDir" ]; then
    cp -r "$Dir/../$ProjectLibDir/"* "$Mod"
fi

if [ -d "$Dir/../$ProjectResDir" ]; then
    cp -r "$Dir/../$ProjectResDir/"* "$Mod"
fi

# Remove .gitkeep and README.md
find "$Temp" \( -iname ".gitkeep" -o -iname "README.md" \) -delete

# Create .zip, remove temp folder
(cd "$Temp" && find . | zip -9@q "$Build/$Package")
rm -rf "$Temp"
