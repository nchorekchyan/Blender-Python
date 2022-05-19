#Script based on https://studio.blender.org/training/scripting-for-artists/ 
#Create 600 Suzanne Primitives, add a modifier, shade smooth

#Import Blender Python
import bpy

#Loop 600 objects
for idx in range(600):
    #Math for x y coordinates dependant on the number we are on
    x = idx % 25
    y = idx // 25
    
    #Create the primitives with a set size and locatio
    bpy.ops.mesh.primitive_monkey_add(size=0.2, location=(x, y, 1))
    
    #Add a subsurf modifier and shade hte object smooth
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()