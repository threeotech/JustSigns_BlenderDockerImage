import bpy

# Register the addon and enable it
bpy.ops.preferences.addon_install(filepath='./auto_rig_pro-master.zip')
bpy.ops.preferences.addon_enable(module='auto_rig_pro-master')
bpy.ops.wm.save_userpref()