#Script based on https://studio.blender.org/training/scripting-for-artists/ 

#Import Blender Python
import bpy

# Select all hidden objects that have '.00' in their name

#Deselect everything
bpy.ops.object.select_all(action='DESELECT')

#Loop for all objects in the scene
for ob in bpy.context.scene.objects:
    
    #Not Hidden, Exit Loop
    if not ob.hide_get():
        continue
    
    #String .00 not in the name, Exit Loop
    if '.00' not in ob.name:
        continue
    
    #Unhide then select    
    ob.hide_set(False)
    ob.select_set(True)