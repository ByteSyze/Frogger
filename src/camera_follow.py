import bge
import bpy

from bge import logic

def main():
    
    controller = bge.logic.getCurrentController()
    scene = logic.getCurrentScene()
    
    camera = scene.cameras["Camera"]
    frog = controller.owner
    
    camera.worldPosition.x = frog.worldPosition.x
    camera.worldPosition.y = frog.worldPosition.y
    
main()