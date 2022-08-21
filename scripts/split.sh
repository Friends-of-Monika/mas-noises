#!/bin/sh

## CONFIG
PART_SIZE=5242880
PART_SIZE_TOLERATION=0.1


## SCRIPT MAIN

get_duration() {
    ffprobe -i "$1" -show_entries format=duration -v quiet \
        -of default=noprint_wrappers=1:nokey=1
}

get_size() { du -b "$1" | awk '{ print $1 }'; }

get_rel_path() { realpath --relative-to="$dir" "$1"; }

dir="$(dirname "$(CDPATH="" cd -- "$(dirname -- "$0")" && pwd)")"
find "$dir/res/audio" -mindepth 1 -type f -iname "*.ogg" | while read -r file; do
    if [ "$(get_size "$file")" -gt "$(echo "$PART_SIZE + $PART_SIZE * $PART_SIZE_TOLERATION" | bc | cut -f1 -d.)" ]; then
        printf "File %s is too big! (%d > %d)\n" "$(get_rel_path "$file")" "$(get_size "$file")" "$PART_SIZE"

        curr_dur=0
        full_dur="$(get_duration "$file")"
        part=1

        while [ "$(echo "$curr_dur < $full_dur" | bc -l)" -eq 1 ]; do
            printf "Splitting (%s parts so far...)\n" "$part"

            part_file="${file%%.*}.$part.${file##*.}"
            ffmpeg -y -v warning -ss "$curr_dur" -i "$file" -fs "$PART_SIZE" -c:a copy "$part_file" </dev/null

            curr_dur="$(echo "$curr_dur + $(get_duration "$part_file")" | bc)"
            part="$((part + 1))"

        done

        printf "\n"
        rm "$file"
    fi
done