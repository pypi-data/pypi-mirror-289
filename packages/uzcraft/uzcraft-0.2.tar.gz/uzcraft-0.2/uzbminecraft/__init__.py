from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
app = Ursina()
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='white_cube.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,
            color=color.lime,
            scale=1,
            origin_y=0.5,
        )
    def input(self, key):
        if self.hovered:
            distance = math.dist(player.position, self.position)
            if distance <= 10:
                if key == 'left mouse down':
                    voxel = Voxel(position=self.position + mouse.normal, texture='white_cube.png')
                if key == 'right mouse down':
                    destroy(self)
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController(position_y=2)
player.scale = (0.9, 0.9, 0.9)
player.speed = 7
sky = Sky()
player.jump_height = 1.4
app.run()
