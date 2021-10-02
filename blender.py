import bpy
from mathutils import Euler

model = bpy.data.objects['model']

for i in range(1, 31):
    model.delta_rotation_euler = Euler((0.0, 0.0, (i-1)*12.0), 'XYZ')

    bpy.context.scene.render.filepath = f"blender/renders/{i:03}.png"
    bpy.ops.render.render(write_still=True)