#############################
##
##  Root Motion Fixer Thingy
##  
##  This script is designed to remove root motion from
##  an animation. The final result should be a very similar
##  animation with no translation in the specified axis. 
##
##  Created by Tyler Hackett (C) 2015
##
#############################

import bpy

x_axis = 0
y_axis = 1
z_axis = 2

start_frame = 0  ## First frame of the animation
end_frame   = 25 ## Last frame of the animation

armature_name   = "Frog_Armature2"
root_name       = "spine"           ## Bone with root motion
axis            = y_axis            ## Axis to remove motion from

scene           = bpy.context.scene

def remove_root_motion(armature_name, root_name):

    armature = bpy.data.objects[armature_name].data
    root_bone = bpy.context.object.pose.bones["spine"]
    
    for frame in range(start_frame,end_frame):
        scene.frame_set(frame)
        print(root_bone.matrix)
        
    
remove_root_motion(armature_name, root_name)