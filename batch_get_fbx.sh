#!/bin/bash

search_dir="$1"
output="$2"
for entry in `ls $search_dir`; do
    blender --background --python import_universal.py -- "$entry" "$output" "$search_dir"
done


