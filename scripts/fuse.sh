#!/bin/sh

dir="$(dirname "$(CDPATH="" cd -- "$(dirname -- "$0")" && pwd)")"
prefix="$dir/res/audio"

file_list="$(mktemp)"
concat_file="$(mktemp)"
find "$prefix" -mindepth 1 -type f -iname "*.ogg" | rev | cut -f1 -d/ | rev | LC_COLLATE=C sort -Vu > "$file_list"
trap 'rm "$file_list" "$concat_file"' EXIT

get_name() { echo "$1" | cut -f1 -d.; }

while read -r file; do
    if [ -z "$curr_file" ]; then
        curr_file="$(get_name "$file")"
    fi

    if [ "$curr_file" = "$(get_name "$file")" ]; then
        printf "file '%s'\n" "$prefix/$file" >> "$concat_file"
    else
        printf "Fusing together file %s.ogg...\n" "$curr_file"
        ffmpeg -y -v warning -f concat -safe 0 -i "$concat_file" -c copy "$prefix/$curr_file.ogg" </dev/null

        truncate -s 0 "$concat_file"
        curr_file="$(get_name "$file")"
        printf "file '%s'\n" "$prefix/$file" >> "$concat_file"
    fi
done < "$file_list"

while read -r file; do rm "$prefix/$file"; done < "$file_list"