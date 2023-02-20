import PySimpleGUI as sg
import arcade
import pymunk
import ursina
import os.path
import os
from PIL import Image
import io
from time import sleep
import arcade
import random
import math
import numpy

"""
RESOURCES
-----------------
https://www.jetbrains.com/help/pycharm/symbols.html#data-sources
https://api.arcade.academy/en/latest/examples/platform_tutorial/step_09.html
https://api.arcade.academy/en/latest/examples/sprite_bullets_aimed.html#sprite-bullets-aimed
https://api.arcade.academy/en/2.6.3/tutorials/pymunk_platformer/index.html#pymunk-platformer-tutorial
"""

#value[x] = 1st text input box
#value[y] = 2nd text input box
#value[z] = slider value
#value[a] = text combo box for calculator
#value[b] = calculator function

sg.theme("DarkAmber")
layout = [
          [sg.Text("Type something here and press OK to enter"), sg.InputText(key = 'x')],
          [sg.Text("Type something else here and press Ok to enter"), sg.InputText(key = 'y', size = (41, 5))],
          [sg.InputCombo(("Calculator", "Pong", "Input Thingy", "Testing Window", "Theme viewer", "Image Viewer", "2D Shooter", "Flappy Sprite"), key = 'a', default_value = "2D Shooter")],
          #if it doesn't work in future things, try adding back the dashes like in the doc ex. (key = '-x-')
          [sg.Text("Slider thingy"), sg.Slider(range = (1, 100), key = ('z'))],
          [sg.Button("OK")],
          [sg.Button("Close")]
]
window = sg.Window("App Launcher", layout)
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "OK" and values['a'] == "Input Thingy":
        sg.popup("You entered", values['x'],
                "You also entered", values['y'],
                "Slider was set to", values['z']
                )

    if event == "OK" and values['a'] == "Calculator":
        layout = [
            [sg.Text("Calculator")],
            [sg.InputCombo(("Addition", "Subtraction", "Multiplication", "Division"), default_value = "Addition", key = ('b'))],
            [sg.Text("Number 1"), sg.InputText(key = '1')],
            [sg.Text("Number 2"), sg.InputText(key = '2')],
            [sg.Button("Calculate")], [sg.Button("Quit")]
        ]
        window = sg.Window("Calculator", layout)
        while True:
            event, values = window.read()
            if event == "Calculate" and values['b'] == "Addition":
                try:
                    x = float(values['1'])
                    y = float(values['2'])
                    [sg.popup("The result was", x + y)]
                except:
                    [sg.popup("Please make sure all values are in decimal form")]
            if event == "Calculate" and values['b'] == "Subtraction":
                try:
                    x = float(values['1'])
                    y = float(values['2'])
                    [sg.popup("The result was", x - y)]
                except:
                    [sg.popup("Please make sure all values are in decimal form")]
            if event == "Calculate" and values['b'] == "Multiplication":
                try:
                    x = float(values['1'])
                    y = float(values['2'])
                    [sg.popup("The result was", x * y)]
                except:
                    [sg.popup("Please make sure all values are in decimal form")]
            if event == "Calculate" and values['b'] == "Division":
                try:
                    x = float(values['1'])
                    y = float(values['2'])
                    [sg.popup("The result was", x / y),
                     "(Top text box/ bottom text box)"]
                except:
                    [sg.popup("Please make sure all values are in decimal form")]
            if event == "Quit" or event == sg.WIN_CLOSED:
                window.close()
                break

    if event == "OK" and values['a'] == "Pong":
        layout = [
            [sg.Text("Use WASD to move left paddle and arrow keys to move right paddle")],
            [sg.Button("Quit")]
        ]
        window = sg.Window("Pong", layout)
        while True:
            event, values = window.read()
            if event == "Quit" or event == sg.WIN_CLOSED:
                window.close()
                break
    """#THE FOLLOWING QUOTED SECTION IS NOT MY CODE
    if event == "OK" and values ['a'] == "Testing Window":
        left_column = [
            [sg.InputText()],
            [sg.Listbox(values = [], size = (25, 10), key = 'File List', enable_events = True)],
            [sg.FileBrowse()],
            [sg.Button("Close")]
        ]
        right_column = [
            [sg.Text(key = "rtext")],
            [sg.Image(key = 'Image')]
            ]

        layout = [
            [sg.Column(left_column),#here if the v/h separators don't work, try putting another bracket and don't
            sg.VSeparator(),#put the brackets in between
            sg.Column(right_column)
             ]
        ]
        window = sg.Window("Testing Window", layout)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Folder":
                folder = values["Folder"]
                try:
                    file_list = os.listdir(folder)
                except:
                    file_list[a]
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".gif"))
                ]
                window["File List"].update(fnames)
            elif event == "File List":
                try:
                    filename = os.path.join(
                        values["Folder"], values["File List"][0]
                    )
                    window["rtext"].update(filename)
                    window["Image"].update(filename = filename)
                except:
                    pass
            window.close

    if event == "OK" and values['a'] == "Theme viewer":
        layout = [[sg.Text("Different themes")],
                  [sg.Text("Click on different theme names to look at them")],
                  [sg.Listbox(values=sg.theme_list(), key='a', enable_events=True, size=(20, 10), default_values="Black")],
                  [sg.Button("Ok")],
                  [sg.Button("Close")]
                  ]
        window = sg.Window("Theme viewer", layout)

        while True:
            event, values = window.read()
            if event == "Close" or event == sg.WIN_CLOSED:
                break
            if event == "Ok":
                sg.theme(values['a'][0])
                sg.popup_get_text("This is {}".format(values['a'][0]))
        window.close()
        exit()

    if event == "OK" and values['a'] == "Image Viewer":
        layout = [
            sg.FileBrowse(),
            sg.Button("Load"),
            sg.InputText(key="filename"),
            sg.Image(key="-IMAGE-")
        ]
        window = sg.Window(layout)
        while True:
            event, values = window.read()
    """

    if event == "OK" and values['a'] == "Flappy Sprite":
        import arcade
        import pymunk

        playerspriteimg = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        class FlappySprite(arcade.Window):
            def __init__(self):
                super().__init__(720, 720, "Flappy Sprite")
                self.bird = None
                self.birdlist = None
                self.boundspritelist = None
                self.tbarrier = None
                self.bbarrier = None
                self.tblist = None
                self.bblist = None
                self.dead = False
                self.tlist = None
                self.blist = None
                self.score = None
            def setup(self):
                self.bird = arcade.Sprite(playerspriteimg, 0.5)
                self.bird.center_x = 128
                self.bird.center_y = 360
                self.birdlist = arcade.SpriteList()
                self.birdlist.append(self.bird)

                self.tblist = arcade.SpriteList()
                self.bblist = arcade.SpriteList()

                self.dead = False

                self.score = 0

                self.tlist = []
                self.blist = []
                for i in range(0, 3):
                    self.tbarrier = arcade.Sprite(":resources:images/tiles/grassMid.png")
                    self.bbarrier = arcade.Sprite(":resources:images/tiles/grassMid.png")
                    self.tbarrier.center_x = 784
                    self.tbarrier.center_y = 784 - (128 * i)
                    self.bbarrier.center_x = 784
                    self.bbarrier.center_y = -64 + (128 * i)
                    self.tblist.append(self.tbarrier)
                    self.tlist.append(self.tbarrier.center_y)
                    self.bblist.append(self.bbarrier)
                    self.blist.append(self.bbarrier.center_y)

                self.boundspritelist = arcade.SpriteList()

                self.w_p_engine = arcade.PymunkPhysicsEngine()

                for i in range(0, 720, 64):
                    top = arcade.Sprite(":resources:images/tiles/grassMid.png", 0.5)
                    bottom = arcade.Sprite(":resources:images/tiles/grassMid.png", 0.5)
                    top.center_x = i
                    top.center_y = 752
                    bottom.center_x = i
                    bottom.center_y = -32
                    self.boundspritelist.append(top)
                    self.boundspritelist.append(bottom)

                def cf(c, d, arbiter, space, data):
                    self.dead = True
                self.w_p_engine.add_collision_handler("a", "b", post_handler=cf)

                #self.p_engine = arcade.physics_engines.PhysicsEnginePlatformer(self.bird, walls = self.boundspritelist, gravity_constant = 0.5)
                self.w_p_engine.add_sprite_list(self.boundspritelist, friction = 0, body_type= pymunk.Body.KINEMATIC, collision_type="a")
                self.w_p_engine.add_sprite_list(self.tblist, friction = 0, body_type= pymunk.Body.KINEMATIC, collision_type="a")
                self.w_p_engine.add_sprite_list(self.bblist, friction = 0, body_type= pymunk.Body.KINEMATIC, collision_type="a")
                self.w_p_engine.add_sprite(self.bird, friction = 0, gravity = (0, -30), body_type= pymunk.Body.DYNAMIC, collision_type="b")

            def on_draw(self):
                arcade.start_render()
                #self.birdlist.draw()
                self.bird.draw()
                self.tblist.draw()
                self.bblist.draw()
                self.boundspritelist.draw()
                if self.dead:
                    arcade.draw_text("YOU DIED! Press \"r\"", color=arcade.color.WHITE, start_x = 30, start_y = 400, font_size = 50, bold = True)
                    arcade.draw_text("to restart", color = arcade.color.WHITE, start_x = 30, start_y = 320, font_size = 50, bold = True)
                arcade.draw_text(f"Score: {self.score}", color=arcade.color.WHITE, start_x=15, start_y=15, font_size=15, bold=True)
            def on_key_press(self, key, modifiers: int):
                if key == arcade.key.SPACE:
                    #if self.p_engine.can_jump():
                    self.w_p_engine.set_velocity(self.bird, velocity = (0, 100))
                if key == arcade.key.R:
                    if self.dead:
                        self.setup()
                    else:
                        pass

            def on_close(self):
                arcade.close_window()

            def on_update(self, delta_time: float):
                self.tbi = 0
                self.tbo = 0
                for sprite in self.tblist:
                    self.tbo += 1
                    #print(self.bo)
                    l = self.tlist
                    self.w_p_engine.set_velocity(sprite, velocity = (-50, 0))
                    if sprite.center_x < -64:
                        """
                        if sprite.center_y == 688:
                            self.w_p_engine.set_position(sprite, (752, sprite.center_y))
                        """
                        if self.tbo == 2:
                            i = random.randrange(1, 3)
                            self.tbi = i
                            i *= 128
                            x = self.tbo - 1
                            self.w_p_engine.set_position(sprite, (784, l[x] - ((3 - (self.tbi + 1)) * 128)))
                            if self.tbi == 1 and self.bbi != 1:
                                self.w_p_engine.set_position(sprite, (784, l[x] - (3 * 128)))
                        elif self.tbo == 3:
                            x = self.tbo - 1
                            self.w_p_engine.set_position(sprite, (784, l[x] + (3 - (self.tbi + 1)) * 128))
                            self.score += 1

                self.bbi = 0
                self.bbo = 0
                for sprite in self.bblist:
                    self.bbo += 1
                    #print(self.bo)
                    l = self.blist
                    self.w_p_engine.set_velocity(sprite, velocity = (-50, 0))
                    if sprite.center_x < -64:
                        """
                        if sprite.center_y == 688:
                            self.w_p_engine.set_position(sprite, (752, sprite.center_y))
                        """
                        if self.bbo == 2:
                            i = random.randrange(1, 3)
                            self.bbi = i
                            i *= 128
                            x = self.bbo - 1
                            self.w_p_engine.set_position(sprite, (784, l[x] + ((3 - (self.bbi + 1)) * 128)))
                            if self.bbi == 1 and self.tbi != 1:
                                self.w_p_engine.set_position(sprite, (784, l[x] + (3 * 128)))
                        elif self.bbo == 3:
                            x = self.bbo - 1
                            self.w_p_engine.set_position(sprite, (784, l[x] - (3 - (self.bbi + 1)) * 128))

                if self.dead:
                    self.w_p_engine.set_velocity(self.bird, velocity = (0, 0))
                    for sprite in self.tblist:
                        self.w_p_engine.set_velocity(sprite, velocity = (0, 0))
                    for sprite in self.bblist:
                        self.w_p_engine.set_velocity(sprite, velocity = (0, 0))

                #self.p_engine.update()
                self.w_p_engine.step(delta_time=1 / 10, resync_sprites=True)

        def main():
            game = FlappySprite()
            game.setup()
            arcade.run()
        if __name__ == "__main__":
            main()



    if event == "OK" and values['a'] == "2D Shooter":
        import arcade

        spritescalingplayer = 0.5
        spritescalingcoin = 0.4
        spritescalingtile = 0.5
        spritescalinggun = 0.3
        spritescalingbullet = 0.35
        movespeed = 4
        jumpspeed = 15
        bulletspeed = 10
        djump = True#double jump
        gravity = 1
        screen_width = 800
        screen_height = 600
        screen_title = "WASD sprite movement"
        leftvmargin = 200
        rightvmargin = 200
        topvmargin = 64
        bottomvmargin = 64
        spawn_x = 64
        spawn_y = 96
        level_one = ":resources:tiled_maps/tiled_map_9.json"
        level_two = ":resources:tiled_maps/test_map_7.json"
        level_three = ":resources:tiled_maps/test_map_3.json"
        level_four = ":resources:tiled_maps/test_map_4.json"
        level_five = ":resources:tiled_maps/test_map_5.json"
        level_six = ":resources:tiled_maps/test_map_6.json"
        uspathash = "\"use_spacial_hash\""
        #slime_layer = arcade.load_tilemap(level_one)

        class sprite_movement(arcade.Sprite):
            def update(self):
                self.center_x += self.change_x
                self.center_y += self.change_y
                if self.left < 0:
                    self.left = 0
                elif self.right > screen_width - 1:
                    self.right = screen_width - 1
                if self.bottom < 0:
                    self.bottom = 0
                elif self.top > screen_height - 1:
                    self.top = screen_height - 1


        class game(arcade.Window):
            def __init__(self):
                super().__init__(screen_width, screen_height, screen_title)
                self.playerspritelist = None
                self.playerspriteinfo = None
                self.zombiespritelist = None
                self.zombiespriteinfo = None
                self.coinspritelist = None
                self.coinspriteinfo = None
                self.slimespritelist = None
                self.slimespriteinfo = None
                self.slimelayer = None
                self.wall_list = arcade.SpriteList(use_spatial_hash = True)
                self.physics_engine = False
                self.physics_engine_zombie = False
                self.physics_engine_slime = None
                self.set_mouse_visible(True)
                self.w_pressed = False
                self.a_pressed = False
                self.s_pressed = False
                self.d_pressed = False
                self.r_pressed = False
                self.q_pressed = False
                self.space_pressed = False
                self.t_pressed = False
                self.jump = False
                self.leftview = 0
                self.bottomview = 0
                self.left_passline = 384
                self.right_passline = 448
                self.level = 0
                self.tile_map = None
                self.mapspriteinfo = None
                self.mapspritelist = None
                self.gunspriteinfo = None
                self.gunspritelist = None
                self.bulletspriteinfo = None
                self.bulletspritelist = None
                self.current_level = 1
                self.dead = False
                self.mouse_x = 0
                self.mouse_y = 0
                self.mouse_pressed = False
                self.coin_counter = 0
                self.opposite_gravity = False
                self.jumpspeed = 15
                self.scene = None
                self.splist = None

                arcade.set_background_color(arcade.color.ARSENIC)

            def setup(self):
                screen_width = 800 #redundancy is for "UnboundLocalError: local variable 'screen_width' referenced before assignment
                screen_height = 600
                #screen_width, screen_height = self.get_size()#fullscreen correct scaling no stretching
                self.playerspritelist = arcade.SpriteList(use_spatial_hash = True)
                playerspriteimg = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
                self.playerspriteinfo = arcade.Sprite(playerspriteimg, spritescalingplayer)
                self.playerspriteinfo.center_x = spawn_x
                self.playerspriteinfo.center_y = spawn_y
                self.playerspritelist.append(self.playerspriteinfo)

                self.zombiespritelist = arcade.SpriteList(use_spatial_hash = True)
                zombiespriteimg = ":resources:images/animated_characters/zombie/zombie_idle.png"
                self.zombiespriteinfo = arcade.Sprite(zombiespriteimg, spritescalingplayer)
                self.zombiespriteinfo.center_x = spawn_x + 50
                self.zombiespriteinfo.center_y = spawn_y
                self.zombiespritelist.append(self.zombiespriteinfo)

                self.coinspritelist = arcade.SpriteList(use_spatial_hash = True)

                self.gunspritelist = arcade.SpriteList(use_spatial_hash = True)
                gunspriteimg = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
                self.gunspriteinfo = arcade.Sprite(gunspriteimg, spritescalinggun)
                self.gunspriteinfo.center_x = self.playerspriteinfo.center_x + 10
                self.gunspriteinfo.center_y = self.playerspriteinfo.center_y
                self.gunspritelist.append(self.gunspriteinfo)

                self.bulletspritelist = arcade.SpriteList(use_spatial_hash=True)
                bulletspriteimg = ":resources:images/space_shooter/laserBlue01.png"
                self.bulletspriteinfo = arcade.Sprite(bulletspriteimg, spritescalingbullet)
                self.bulletspriteinfo.center_x = self.playerspriteinfo.center_x + 10
                self.bulletspriteinfo.center_y = self.playerspriteinfo.center_y
                self.bulletspritelist.append(self.bulletspriteinfo)
                self.bulletspriteinfo.scale = 0

                self.slimespritelist = arcade.SpriteList(use_spatial_hash=True)
                #slimelayerlist = arcade.SpriteList(slime_layer.sprite_lists["Slime Layer 1"])
                #self.slimespritelist.append(self.slimespriteinfo)
                #self.slimespritelist = slimelayerlist.sprite_list["Slime Layer 1"]

                #slayer = arcade.tilemap.read_tmx(level_one)
                #self.slimespritelist = arcade.tilemap._process_object_layer(slayer, "Slime Layer 1", 1)
                #self.slimespritelist = arcade.tilemap.
                #slayer.

                """
                olayer = {
                    "Slime Layer 1": {uspathash: True, "scaling": 1}
                }
                self.slimespriteinfo = arcade.load_tilemap(level_one, spritescalingtile, olayer)
                self.slimespritelist = arcade.Scene.from_tilemap(self.slimespriteinfo)
                """


                """
                for i in range(1, 100):
                    coinspriteimg = arcade.Sprite(":resources:/images/items/coinGold.png", spritescalingcoin)
                    coinspriteimg.center_x = random.randrange(self.leftview, self.leftview + screen_width) #spawn within viewport so if it hits the viewport it's gonna die and respawn inside the viewport when it moves
                    coinspriteimg.center_y = random.randrange(64, self.bottomview + screen_height)
                    self.coinspritelist.append(coinspriteimg)
                    for coinspriteimg in self.coinspritelist:
                        if coinspriteimg.center_x - coinspriteimg.center_x > 0:
                            print("hi")
                        else:
                            pass
                """
                """
                for x in range(-209, 832, 64): #use this to turn off auto map generation i think
                    wall = arcade.Sprite(":resources:images/tiles/grassMid.png", spritescalingtile)
                    wall.center_x = x
                    wall.center_y = 32
                    self.wall_list.append(wall)
                """

                def map_gen():
                    self.playerspriteinfo.center_x = spawn_x
                    self.playerspriteinfo.center_y = spawn_y
                    self.zombiespriteinfo.center_x = spawn_x + 50
                    self.zombiespriteinfo.center_y = spawn_y
                    layer = {"Tile Layer 1": {"use_spatial_hash": True}}
                    self.mapspriteinfo = arcade.load_tilemap(tile_map, spritescalingtile, layer)
                    self.mapspritelist = arcade.Scene.from_tilemap(self.mapspriteinfo)
                    self.physics_engine = arcade.PhysicsEnginePlatformer(self.playerspriteinfo, gravity_constant=gravity, walls=self.mapspritelist["Platforms"])
                    self.physics_engine_zombie = arcade.PhysicsEnginePlatformer(self.zombiespriteinfo, gravity_constant = gravity, walls = self.mapspritelist["Platforms"])
                    #self.physics_engine_slime = arcade.PhysicsEnginePlatformer(self.mapspritelist["Slime Layer 1"], walls = self.mapspritelist["Platforms"])

                def nmapgen():
                    self.dead = False
                    #tile_map = level_one
                    self.playerspriteinfo.center_x = spawn_x
                    self.playerspriteinfo.center_y = spawn_y
                    self.zombiespriteinfo.center_x = spawn_x + 50
                    self.zombiespriteinfo.center_y = spawn_y
                    # layer = {"Tile Layer 1": {"use_spatial_hash": True}}
                    if tile_map == level_one:
                        layer_list = {
                            "Tile Layer 1": {uspathash: True},
                            "Kill Layer 1": {uspathash: True},
                            "No Hit Layer 1": {uspathash: True},
                            "Jump Layer 1": {uspathash: True, "offset": (-0.5, -5)},
                            # https://api.arcade.academy/en/latest/_modules/arcade/tilemap/tilemap.html
                            "Level Layer 1": {uspathash: True},
                            "Coin Layer 1": {uspathash: True},
                            "Slime Layer 1": {uspathash: True, "scaling": spritescalingtile * 1}
                        }
                    else:
                        layer_list = {
                            "Tile Layer 1": {uspathash: True},
                            "Kill Layer 1": {uspathash: True},
                            "No Hit Layer 1": {uspathash: True},
                            "Jump Layer 1": {uspathash: True, "offset": (-0.5, -5)},
                            "Level Layer 1": {uspathash: True}
                            # https://api.arcade.academy/en/latest/_modules/arcade/tilemap/tilemap.html
                        }
                    self.mapspriteinfo = arcade.load_tilemap(tile_map, spritescalingtile, layer_list)
                    self.mapspritelist = arcade.Scene.from_tilemap(self.mapspriteinfo)
                    self.physics_engine = arcade.PhysicsEnginePlatformer(self.playerspriteinfo, gravity_constant=gravity, walls=self.mapspritelist["Tile Layer 1"])  # gravity controls the increase of the downward speed of the sprite per frame ie. acceleration; "jump function" checks for a single press and doesn't account for the key being held down so it always decelerates from the initial upwards speed
                    self.physics_engine_zombie = arcade.PhysicsEnginePlatformer(self.zombiespriteinfo, gravity_constant=gravity, walls=self.mapspritelist["Tile Layer 1"])
                    #self.physics_engine_slime = arcade.PhysicsEnginePlatformer(self.mapspritelist["Slime Layer 1"], gravity_constant=gravity, walls = self.mapspritelist["Tile Layer 1"])
                    #self.pymunk_physics_engine = arcade.PymunkPhysicsEngine()
                    #self.pymunk_physics_engine.add_sprite(self.slimespritelist, body_type=arcade.PymunkPhysicsEngine.DYNAMIC)

                    self.physics_engine_slime = arcade.PymunkPhysicsEngine()

                    self.splist = []
                    for slime in self.mapspritelist["Slime Layer 1"]:
                        self.slimespritelist.append(slime)
                        self.splist.append(slime.center_x)
                    self.physics_engine_slime.add_sprite_list(self.slimespritelist, friction = 0, body_type = pymunk.Body.KINEMATIC, collision_type = "a")


                if self.current_level == 1:
                    tile_map = level_one
                    nmapgen()
                if self.current_level == 2:
                    tile_map = level_two
                    #map_gen()
                    nmapgen()
                if self.current_level == 3:
                    tile_map = level_three
                    #map_gen()
                    nmapgen()



            def on_key_press(self, key, modifiers: int):
                if key == arcade.key.T:#maybe use this whole block for clarity instead of using the one liner until you fully understand how it works
                    if self.fullscreen == False:
                        self.set_fullscreen()
                        #screen_width, screen_height = self.get_size()  # correct scaling no stretching; might hafta also apply to the viewport changing from movement stuff cause it loses its scaling when the original viewport changes; must put it after "self.set_fullscreen()" etc.
                        arcade.set_viewport(self.leftview, self.leftview + screen_width, self.bottomview, self.bottomview + screen_height)
                    elif self.fullscreen == True:
                        self.set_fullscreen(not self.fullscreen)#sets the mode to not be fullscreen between being fullscreen and not fullscreen; "not self.fullscreen" as the opposite function of "self.set.fullscreen"
                if key == arcade.key.SPACE:
                    if djump == True:
                        self.playerspriteinfo.change_y = self.jumpspeed
                    if djump == False:
                        if self.physics_engine.can_jump():#controls multi jump
                            self.playerspriteinfo.change_y = self.jumpspeed
                if key == arcade.key.W:
                    self.w_pressed = True
                elif key == arcade.key.A:
                    self.a_pressed = True
                if key == arcade.key.S:
                    self.s_pressed = True
                elif key == arcade.key.D:
                    self.d_pressed = True
                if key == arcade.key.R:
                    self.r_pressed = True
                if key == arcade.key.Q:
                    self.q_pressed = True

                """
                if key == arcade.key.F:
                    self.set_fullscreen(not self.fullscreen)#fullscreen toggle
                    screen_width, screen_height = self.get_size()#correct scaling no stretching
                    arcade.set_viewport(self.leftview, self.leftview + screen_width, self.bottomview, self.bottomview + screen_height)
                """

            def on_key_release(self, key, modifiers: int):
                if key == arcade.key.SPACE:
                    self.jump = False
                if key == arcade.key.W:
                    self.w_pressed = False
                elif key == arcade.key.A:
                    self.a_pressed = False
                if key == arcade.key.S:
                    self.s_pressed = False
                elif key == arcade.key.D:
                    self.d_pressed = False
                if key == arcade.key.R:
                    self.r_pressed = False

            def on_mouse_motion(self, x, y, dx, dy):
                self.mouse_x = x + self.leftview
                self.mouse_y = y + self.bottomview

            def on_mouse_press(self, x, y, button, modifiers):
                bulletspriteimg = ":resources:images/space_shooter/laserBlue01.png"
                self.bulletspriteinfo = arcade.Sprite(bulletspriteimg, spritescalingbullet)
                self.bulletspriteinfo.center_x = self.playerspriteinfo.center_x
                self.bulletspriteinfo.center_y = self.playerspriteinfo.center_y
                x_diff = self.mouse_x - self.playerspriteinfo.center_x
                y_diff = self.mouse_y - self.playerspriteinfo.center_y
                radangle = math.atan2(y_diff, x_diff)#use atan2 instead of atan(y_diff / x_diff) because atan2 takes into account of the signs of the values so it can output "proper values"
                self.bulletspriteinfo.angle = math.degrees(radangle)#original angle/radangle is in radians; use math.degrees() to convert it to degrees so the actual sprite angle is assigned to a degree value
                self.bulletspriteinfo.change_x = math.cos(radangle) * bulletspeed
                self.bulletspriteinfo.change_y = math.sin(radangle) * bulletspeed
                self.bulletspritelist.append(self.bulletspriteinfo)

            def on_mouse_release(self, x, y, button, modifiers):
                self.mouse_pressed = False

            def on_draw(self):
                arcade.start_render()
                self.wall_list.draw()
                self.coinspritelist.draw()
                self.mapspritelist.draw()
                if self.dead:
                    arcade.draw_text("YOU DIED! Press \"r\"", color=arcade.color.BLACK, start_x = self.leftview + screen_width // 2 - 330, start_y = self.bottomview + screen_height // 2 + 30, font_size = 50, bold = True)
                    arcade.draw_text("to restart", color = arcade.color.BLACK, start_x = self.leftview + screen_width // 2 - 135, start_y = self.bottomview + screen_height // 2 - 65, font_size = 50, bold = True)
                self.playerspritelist.draw()#render the player last so the sprite will appear on top of all the other sprites
                self.zombiespritelist.draw()
                #self.gunspritelist.draw()
                self.bulletspritelist.draw()
                self.slimespritelist.draw()
                arcade.draw_text(text = f"Coords: {str(int(self.playerspriteinfo.center_x))}, {str(int(self.playerspriteinfo.center_y))}", color=arcade.color.WHITE, start_x = self.leftview + 10, start_y = self.bottomview + 10, font_size = 15, bold = True)#comma between the two coords is part of the string and not to actually separate the two coords as individual variables; the f string function uses the curly brackets/braces
                arcade.draw_text(text = (self.mouse_x, self.mouse_y), color=arcade.color.WHITE, start_x = self.leftview + 10, start_y = self.bottomview + 35, font_size = 15, bold = True)
                arcade.draw_text(text = int(self.bulletspriteinfo.angle), color=arcade.color.WHITE, start_x = self.leftview + 10, start_y = self.bottomview + 60, font_size = 15, bold = True)
                arcade.draw_text(text = f"Coins: {self.coin_counter}", color=arcade.color.WHITE, start_x = self.leftview + 10, start_y = self.bottomview + 85, font_size = 15, bold = True)

            def on_close(self):
                arcade.close_window()

            def on_update(self, delta_time):
                if self.r_pressed and not self.dead:
                    self.setup()
                for coinspriteimg in self.coinspritelist:
                    coinspriteimg.change_x = 0
                    coinspriteimg.change_y = 0
                self.playerspriteinfo.change_x = 0
                #self.playerspriteinfo.change_y = 0
                self.gunspriteinfo.center_x = self.playerspriteinfo.center_x + 10
                self.gunspriteinfo.center_y = self.playerspriteinfo.center_y
                if self.w_pressed and not self.s_pressed:
                    #self.playerspriteinfo.change_y = movespeed
                    pass
                if self.a_pressed and not self.d_pressed:
                    self.playerspriteinfo.change_x = -movespeed
                if self.s_pressed and not self.w_pressed:
                    #self.playerspriteinfo.change_y = -movespeed
                    pass
                if self.d_pressed and not self.a_pressed:
                    self.playerspriteinfo.change_x = movespeed
                if self.q_pressed:
                    self.opposite_gravity = not self.opposite_gravity
                    if self.opposite_gravity is True:
                        self.jumpspeed = -self.jumpspeed
                        self.physics_engine.gravity_constant = -1
                    if self.opposite_gravity is False:
                        self.physics_engine.gravity_constant = 1
                        self.jumpspeed = -self.jumpspeed
                    self.q_pressed = False

                def coin_spawn():
                    coinspriteimg = arcade.Sprite(":resources:/images/items/coinGold.png", spritescalingcoin)
                    coinspriteimg.center_x = random.randrange(self.leftview, self.leftview + screen_width)
                    coinspriteimg.center_y = random.randrange(self.bottomview + 64, self.bottomview + screen_height)
                    self.coinspritelist.append(coinspriteimg)

                coinplayerhitlist = arcade.check_for_collision_with_list(self.playerspriteinfo, self.coinspritelist)
                for coinspriteimg in coinplayerhitlist:
                    coinspriteimg.remove_from_sprite_lists()
                    coin_spawn()

                """
                coincoinhitlist = arcade.check_for_collision_with_list(coinspriteimg, self.coinspritelist)
                for coinspriteimg in coinplayerhitlist:
                    coinspriteimg.remove_from_sprite_lists()
                    coin_spawn()
                #https://api.arcade.academy/en/development/examples/sprite_no_coins_on_walls.html#sprite-no-coins-on-walls
                """

                for coinspriteimg in self.coinspritelist:
                    if coinspriteimg.center_x > self.leftview + screen_width:
                        coinspriteimg.remove_from_sprite_lists()
                        coin_spawn()
                    if coinspriteimg.center_x < self.leftview:
                        coinspriteimg.remove_from_sprite_lists()
                        coin_spawn()
                    if coinspriteimg.center_y < self.bottomview:
                        coinspriteimg.remove_from_sprite_lists()
                        coin_spawn()
                    if coinspriteimg.center_y > self.bottomview + screen_height:
                        coinspriteimg.remove_from_sprite_lists()
                        coin_spawn()

                """
                wallhitlist = arcade.check_for_collision_with_list(self.playerspriteinfo, self.wall_list)
                for wall in wallhitlist:
                    wall.remove_from_sprite_lists()
                """

                for bulletspriteimg in self.bulletspritelist:
                    if self.current_level == 1:
                        bullethitlist = arcade.check_for_collision_with_list(bulletspriteimg, self.mapspritelist["Tile Layer 1"])
                        for x in bullethitlist:
                            bulletspriteimg.remove_from_sprite_lists()
                    elif self.current_level == 2 or self.current_level == 3:
                        bullethitlist = arcade.check_for_collision_with_list(bulletspriteimg, self.mapspritelist["Tile Layer 1"])
                        for x in bullethitlist:
                            bulletspriteimg.remove_from_sprite_lists()

                """
                class z_movement(xxy):
                    def zright():
                        g = game()
                        g.zombiespriteinfo.change_x = 2
                    def zleft():
                        g = game()
                        g.zombiespriteinfo.change_x = -2
                z_movement = z_movement()
                """
                def zright():
                    self.zombiespriteinfo.change_x = 1
                    return True
                def zleft():
                    self.zombiespriteinfo.change_x = -1
                    return True
                def zjump():
                    if self.physics_engine.can_jump():
                        self.zombiespriteinfo.change_y = jumpspeed
                def zstop():
                    if arcade.check_for_collision_with_list(self.zombiespriteinfo, self.mapspritelist["Jump Layer 1"]):
                        return True
                def zhit():
                    #for zombiespriteimg in self.zombiespritelist:
                        #zombiehitlist = arcade.check_for_collision(zombiespriteimg, self.playerspriteinfo)
                    if zright() and 32 >= self.playerspriteinfo.center_x - self.zombiespriteinfo.center_x > 0 and 32 >= self.playerspriteinfo.center_y - self.zombiespriteinfo.center_y >= 0:
                        self.playerspriteinfo.change_x = 2
                        self.playerspriteinfo.change_y = 2
                    elif zleft() and -32 <= self.playerspriteinfo.center_x - self.zombiespriteinfo.center_x < 0 and 32 >= self.playerspriteinfo.center_y - self.zombiespriteinfo.center_y >= 0:
                        self.playerspriteinfo.change_x = -2
                        self.playerspriteinfo.change_y = 2
                    elif self.playerspriteinfo.center_x - self.zombiespriteinfo.center_x == 0 and 33 >= self.playerspriteinfo.center_y - self.zombiespriteinfo.center_y >= 0:
                        self.playerspriteinfo.change_y = 2
                    else:
                        pass
                class zombie_movement():
                    def __init__(self, x, y, xx, yy):
                        super().__init__()
                        self.zx = x
                        self.zy = y
                        self.px = xx
                        self.py = yy
                    def follow(self):
                        if self.zx < self.px:
                            #z_movement.zright()
                            zright()
                        elif self.zx > self.px:
                            #z_movement.zleft()
                            zleft()
                        elif self.zx == self.px:
                            pass
                    def jump(self):
                        if zstop():
                            zjump()
                    def hit(self):
                        zhit()

                zm = zombie_movement(self.zombiespriteinfo.center_x, self.zombiespriteinfo.center_y, self.playerspriteinfo.center_x, self.playerspriteinfo.center_y)
                zm.jump()
                zm.hit()
                zm.follow()

                def slime_movement():
                    x = -1
                    s = self.splist
                    for slime in self.slimespritelist:
                        x += 1
                        #self.physics_engine_slime.set_velocity(slime, (-50, 0))
                        if int(slime.center_x) < int(s[x]) - 50:
                            self.physics_engine_slime.set_velocity(slime, (50, 0))
                        elif int(slime.center_x) == int(s[x]):
                            self.physics_engine_slime.set_velocity(slime, (-50, 0))
                slime_movement()


                def coin_collection():
                    #if arcade.check_for_collision_with_list(self.playerspriteinfo, self.mapspritelist["Coin Layer 1"]):
                    coinobjecthitlist = arcade.check_for_collision_with_list(self.playerspriteinfo, self.mapspritelist["Coin Layer 1"])
                    for x in coinobjecthitlist:
                        x.remove_from_sprite_lists()
                        self.coin_counter += 1
                if self.current_level == 1:
                    coin_collection()



                changed = False#https://api.arcade.academy/en/latest/examples/platform_tutorial/step_05.html scrolling(viewport changing)

                left_boundary = self.leftview + leftvmargin#variable for detecting when to change the viewport
                right_boundary = self.leftview + screen_width - rightvmargin
                top_boundary = self.bottomview + screen_height - topvmargin
                bottom_boundary = self.bottomview + bottomvmargin

                if self.playerspriteinfo.left < left_boundary:#condition to change the viewport
                    self.leftview -= left_boundary - self.playerspriteinfo.left#calculating where to change the leftview(edge of window)
                    changed = True

                    """
                    fit = self.playerspriteinfo.center_x % 320
                    is_fit = fit == 0
                    if is_fit and self.playerspriteinfo.left < int(self.left_passline):
                        for x in range(int(self.playerspriteinfo.left - 320) - 320, int(self.playerspriteinfo.left), 64):
                            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", spritescalingtile)
                            wall.center_x = x
                            wall.center_y = 32
                            self.wall_list.append(wall)
                        l = self.playerspriteinfo.left
                        if self.left_passline > l:#condition for moving the passline
                            self.left_passline = l
                        """

                if self.playerspriteinfo.right > right_boundary:
                    self.leftview += self.playerspriteinfo.right - right_boundary
                    changed = True

                    """
                    fit = self.playerspriteinfo.center_x % 320
                    is_fit = fit == 0
                    if is_fit and self.playerspriteinfo.right > int(self.right_passline):
                        for x in range(int(self.playerspriteinfo.right), int(self.playerspriteinfo.right + 320) + 320, 64):
                            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", spritescalingtile)
                            wall.center_x = x
                            wall.center_y = 32
                            self.wall_list.append(wall)
                        r = self.playerspriteinfo.right
                        if self.right_passline < r:
                            self.right_passline = r
                    """

                if self.playerspriteinfo.top > top_boundary:
                    self.bottomview += self.playerspriteinfo.top - top_boundary
                    changed = True
                if self.playerspriteinfo.bottom < bottom_boundary:
                    self.bottomview -= bottom_boundary - self.playerspriteinfo.bottom
                    changed = True

                if changed == True:
                    self.leftview = int(self.leftview)
                    self.bottomview = int(self.bottomview)
                    arcade.set_viewport(self.leftview, self.leftview + screen_width, self.bottomview, self.bottomview + screen_height) #changing the viewport

                """
                if self.current_level == 1 and self.playerspriteinfo.center_x > 1450 and self.playerspriteinfo.center_y < 170:#replace with variable for map width and map height
                    self.current_level += 1
                    self.setup()

                if self.current_level == 2 and self.playerspriteinfo.center_x > 2200 and self.playerspriteinfo.center_y < 100:
                    self.current_level += 1
                    self.setup()
                """

                def level_up():
                    if arcade.check_for_collision_with_list(self.playerspriteinfo, self.mapspritelist["Level Layer 1"]):
                        self.current_level += 1
                        self.setup()

                if self.current_level == 1:
                    level_up()
                if self.current_level == 2:
                    level_up()

                if self.current_level == 1:
                    if arcade.check_for_collision_with_list(self.playerspriteinfo, self.mapspritelist["Kill Layer 1"]):#use if statements for checking if some function like collision checking is true
                        self.w_pressed = False
                        self.a_pressed = False
                        self.s_pressed = False
                        self.d_pressed = False
                        self.playerspriteinfo.change_x = 0
                        self.playerspriteinfo.change_y = 0
                        self.dead = True
                        if self.r_pressed:
                            self.dead = False
                            self.setup()
                        """
                        #sg.popup("YOU DIED! Press any key or release key to continue.", title = "YOU DIED", any_key_closes = True, button_type = 5)#fix to stop window from closing when the already pressed key is lifted
                        layout = [[sg.Text("YOU DIED! Press \"r\" to restart")]]
                        window = sg.Window("YOU DIED!", layout, return_keyboard_events = True, no_titlebar = True, keep_on_top = True)
                        while True:
                            event, values = window.read()
                            if event == "r" or event == sg.WIN_CLOSED:
                                window.close()
                                self.setup()
                                break
                        """
                    else:
                        pass

                if self.current_level == 1:
                    if self.playerspriteinfo.center_x > 1536 or self.playerspriteinfo.center_x < 0 or self.playerspriteinfo.center_y > 1536 or self.playerspriteinfo.center_y < 0:
                        self.setup()

                self.playerspriteinfo.update()#remember to update everything that needs to be updated
                self.coinspritelist.update()
                self.gunspriteinfo.update()
                self.bulletspritelist.update()#update the whole list instead of a single sprite so all bullets remain in action even after a new bullet spawns
                self.zombiespriteinfo.update()
                #self.slimespritelist.update()
                #self.slimespriteinfo.update()
                #self.slimelayer.update()

                self.physics_engine.update()
                self.physics_engine_zombie.update()
                self.physics_engine_slime.step()

        def main():
            window = game()
            window.setup()
            arcade.run()

        if __name__ == "__main__":
            main()
    if event == "Close" or sg.WIN_CLOSED:
        break
window.close()
exit()

#-------------------------------
def beach():
    arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.CANARY_YELLOW)
def background():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * (1 / 3), arcade.color.BLUE)
    # the (1/3) i think counts from the bottom to up to tell if the 1/3 is on the bottom or top; in this case, it is on the bottom
beach()
background()

#------------------------------