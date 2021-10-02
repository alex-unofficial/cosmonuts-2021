import bpy
from cmath import pi
from mathutils import Vector, Euler

model = bpy.data.objects['216kleopatra']

render_dir = "/home/alex/Desktop/stuff/blender/renders/"

N = 60

for i in range(1, N + 1):
    model.delta_rotation_euler = Euler((0.0, 0.0, (i-1)*2*pi/N), 'XYZ')

    bpy.context.scene.render.filepath = render_dir +  f"{i:03}.png"
    bpy.ops.render.render(write_still=True)