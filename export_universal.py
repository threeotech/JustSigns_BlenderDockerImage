import bpy
import math
import sys
import os

def get_keyframes(obj_list):
    keyframes = []
    for obj in obj_list:
        anim = obj.animation_data
        if anim is not None and anim.action is not None:
            for fcu in anim.action.fcurves:
                for keyframe in fcu.keyframe_points:
                    x, y = keyframe.co
                    if x not in keyframes:
                        keyframes.append((math.ceil(x)))
    return keyframes

path = sys.argv[7]
if not os.path.isdir(path):
    os.makedirs(path)
 # remove unused mesh for faster exporting time
for x in bpy.context.scene.objects:
    if x.name == "Alex_shirt" or x.name == "Alex_jeans" or x.name == "Alex_shoes" or x.name == "Alex_tshirt":
        bpy.data.objects.remove(x)
# bpy.context.scene.arp_export_rig_type = 'humanoid'
bpy.context.scene.arp_export_rig_type = 'mped'
bpy.context.scene.arp_engine_type = 'unity'
bpy.context.scene.arp_export_twist = False
frame = ''
# get all selected objects
selection = bpy.context.selected_objects
scene = bpy.context.scene
# check if selection is not empty
if selection:
    # get all frames with assigned keyframes
    keys = get_keyframes(selection)
    # print(keys)
    string_ints = [str(int) for int in keys]
    frame = "_".join(string_ints)


# bpy.types.Scene.arp_export_end_frame
bpy.ops.id.arp_export_fbx_panel(filepath=f'{path}/{sys.argv[6]}_{frame}.fbx')
print(f'{path}/{sys.argv[6]}_{frame}.fbx')


# bpy.ops.import_scene.fbx(filepath="F:/Blender/2019-04-09-S.fbx")