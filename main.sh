#!/bin/bash

url="$1"

/bin/2.92/python/bin/python3.7m  load_blender.py $url

./batch_export_fbx.sh blender/ fbx/

./batch_get_fbx.sh fbx/ gltf/

/bin/2.92/python/bin/python3.7m  get_gltf_batch.py gltf/ csv/

/bin/2.92/python/bin/python3.7m  uploadkeypoint_universal.py csv/ uploadedwords

/bin/2.92/python/bin/python3.7m  delete_blender.py $url