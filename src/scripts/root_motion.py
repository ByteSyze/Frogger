#############################
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

armature_name   = "Frog_Armature2"
root_name       = "spine"           ##Bone with root motion
axis            = "y"

def root_motion(armature_name, root_name)

    armature = bpy.data.objects[armature_name].data
    root_bone = armature.bones["spine"]

    print(root_bone)
    
root_motion(armature_name, root_name)