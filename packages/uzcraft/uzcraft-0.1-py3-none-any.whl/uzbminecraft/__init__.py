from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

app = Ursina()

grass_texture = load_texture('grass_block.png')
stone_texture = load_texture('stone_block.png')
brick_texture = load_texture('brick_block.png')
dirt_texture = load_texture('dirt_block.png')
sky_texture = load_texture('skybox.png')
arm_texture = load_texture('arm_texture.png')
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
block_pick = 1
window.fps_counter.enabled = False
window.exit_button.visible = False
window.entity_counter.enabled = False
dead_text = None  # Ikkita o'zgaruvchini e'lon qilamiz, ularni update funksiyasida ham ishlatamiz
respawn_text = Text(text="respawn", color=color.red, position=(-0.4, 0.1, 0), scale=(8, 8, 8))
respawn_text.enabled = False  # "respawn" yozuvini boshlang'ich holatda yashirib qo'yamiz
def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if player.position.y < -800:
        respawn()
def respawn():
    global dead_text
    dead_text = Text(text="respawn", color=color.red, position=(-0.4, 0.1, 0), scale=(8, 8, 8))
    invoke(destroy, dead_text, delay=3)  # 3 soniyadan keyin yozuvni yo'q qilish
    player.position = (0, 4, 0)  # Playerni qayta joylashtirish
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
            origin_y=0.5,
        )
    def input(self, key):
        if self.hovered:
            distance = math.dist(player.position, self.position)
            if distance <= 10:
                if key == 'left mouse down':
                    punch_sound.play()
                    if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                    if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                    if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                    if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if key == 'right mouse down':
                    punch_sound.play()
                    destroy(self)
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture="assets/sky.png",
            scale=1500,
            double_sided=True
        )
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)
for z in range(20):
    for x in range(20):
        for i in range(-2, -3, -1):
            under_ground = Voxel(position=(x, -1, z), texture=dirt_texture)
            under_ground2 = Voxel(position=(x, i, z), texture=stone_texture)
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController(position_y=2)
player.scale = (0.9, 0.9, 0.9)
player.speed = 7
def input(key):
    if key == "c":
        if player.scale == (0.9, 0.9, 0.9):
            player.scale = (0.6, 0.6, 0.6)
            player.speed = 3
        else:
            player.scale = (0.9, 0.9, 0.9)
            player.speed = 7
sky = Sky()
hand = Hand()
player.jump_height = 1.4
app.run()
