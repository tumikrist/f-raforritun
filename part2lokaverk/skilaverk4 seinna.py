"""
Better Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
This is slightly better than sprite_move_keyboard.py example
in how it works, but also slightly more complex.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard_better
"""

import arcade
import random

SPRITE_SCALING = 0.5
playerscale=0.2
boxscale=0
bombsprite=0.09

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Better Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5



class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
           self.left = 0
        if self.right > 3000 - 1:
           self.right = 3000 - 1
        #
        if self.bottom < 0:
           self.bottom = 0
        if self.top > 3000 - 1:
           self.top = 3000 - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.baby_list = None
        self.wall_list = None
        self.bomb_list= None

        # Set up the player info
        self.player_sprite = None
        self.babysprite = None

        #self.bobspirte=None

        #makewalls
        self.number_wall = 20

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # This variable holds our simple "physics engine"
        self.physics_engine = None


        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.baby_list= arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.collist=arcade.SpriteList


        #the baby
        self.babysprite = Player("baby.png", playerscale)
        self.babysprite.center_x = random.randint(100,500)
        self.babysprite.center_y = random.randint(100,500)
        self.baby_list.append(self.babysprite)


        # Set up the player
        self.player_sprite = Player("Dababy_cloud.png",playerscale)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.pos_player_X=0
        self.pos_player_Y=0


        for x in range(self.number_wall):
            wall = Player("RTS_Crate.png", playerscale)
            wall.center_x = random.randint(100,2800)
            wall.center_y = random.randint(100,2800)
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.baby_list)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        self.camera_for_sprites.use()


        # Draw all the sprites.
        self.player_list.draw()
        self.baby_list.draw()
        self.wall_list.draw()
        self.bomb_list.draw()

        arcade.draw_rectangle_outline(1500,1500,3000,3000,arcade.color.BLACK,10)

        arcade.draw_text(f"pos : x {self.pos_player_X}: y {self.pos_player_Y}",self.pos_player_X-150, self.pos_player_Y+150, arcade.color.WHITE, 24)

        #camera
        self.camera_for_gui.use()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()

        self.bomb_list.update()
        for bomb in self.bomb_list:
            pass
        #self.scroll_to_player()
        self.pos_player_X=self.player_sprite.center_x
        self.pos_player_Y=self.player_sprite.center_y
        print(self.pos_player_X)

        # Calculate speed based on the keys pressed

        #movement
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        #bomb collide
        for bomb in self.bomb_list:
            # Checkar hvort skot hitti penning
            hit_list = arcade.check_for_collision_with_list(bomb, self.wall_list)

            # ef það gerðist lata skotið hverfa
            if len(hit_list) > 0:
                bomb.remove_from_sprite_lists()

            # fyrir penningin sem við hittum faum við stig
            for box in hit_list:
                box.remove_from_sprite_lists()
                #self.score += 1

                # spilar hljóð ef hitt penning er
                #arcade.play_sound(self.hit_sound)

        self.player_list.update()

        CAMERA_SPEED = 1
        lower_left_corner = (
            self.player_sprite.center_x - self.width / 2,
            self.player_sprite.center_y - self.height / 2,
        )
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        #movment
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        #bomb
        if key==arcade.key.SPACE:
            print("mwow")
            bomb = arcade.Sprite("1200px-AA-3-Anab.png",bombsprite)
            # settur skotið þar sem player er
            start_x = self.pos_player_X-15
            start_y = self.pos_player_Y-20
            bomb.change_y = -30
            bomb.angle=90
            bomb.center_x = start_x
            bomb.center_y = start_y

            self.bomb_list.append(bomb)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()