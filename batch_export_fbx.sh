#!/bin/bash

search_dir="$1"
output="$2"

for entry in `ls $search_dir`; do
    filename="$(cut -d '.' -f 1 <<< $entry)"
    blender --background "$search_dir/$entry" --python export_universal.py -- "$filename" "$output"
done


# ./batch_fbx.sh test_export/