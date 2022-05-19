#Script based on https://studio.blender.org/training/scripting-for-artists/ 
#Deselect objects with '.00' in the name
#Select stuff before running

#Import Blender Python
import bpy

# Create Placeholder list 
to_deselect = []

#Loop deselect objects with .00 in name
for ob in bpy.context.selected_objects:
    if '.00' not in ob.name:
        continue
    
    #Append to list created earlier
    to_deselect.append(ob)
    
#Loop to delselect everything in the list
for ob in to_deselect:
    ob.select_set(False)