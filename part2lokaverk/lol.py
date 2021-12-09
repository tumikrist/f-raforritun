"""
vinna a vinna fra score system
og það er hægt að tappa ef þu runar out of time
og miss munandi erfiðar level 3 missmunadni sem breta numer kassa og tima
hafa check box fyrir erfiðleika og tima
og enda skja þar sem hægt er að endur runa leikinn

og ef timi gefst 3 speed boost sem endast í 3 sec hvert sem fara i gang með að ytta a takka

setja random movement system sem færir hann i random y og x att i random tima
sem er sitt eigið check box
"""

import math
import arcade
import random

SPRITE_SCALING = 0.5
playerscale=0.2
boxscale=0
bombsprite=0.09

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Tumi leikur"

MOVEMENT_SPEED = 5
laser_speed=5
number_wall = 7

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
        #self.number_wall = 3
        self.wall_pos=[]


        #byrjun skjár
        self.startscreen=True

        #endaskjar
        self.endscreen=False
        self.end_timi=False
        self.end_score=False


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
        #player x og y pos

        self.pos_player_X=0
        self.pos_player_Y=0


        #score
        self.score = 0
        #vopn 1
        self.wpn=1

        #timi
        self.timi=0
        self.timi_heild=0
        self.timi_local=0

        self.movecnt = 0

        #unlock wepon 2 code
        self.unlock2=False
        self.textgoawayunlock=False
        self.ecnt=0

        #fyrir vopn 2 þvi það eru 4 skot
        self.shot_rotate = 0
        self.shot_x = 0
        self.shot_y = 0


        self.random_speedlist = []
        for x in range(number_wall):
            temp2 = []
            self.box_x_speed = 0
            self.box_y_speed = 0
            temp2.extend((self.box_x_speed,self.box_y_speed))
            self.random_speedlist.append(temp2)
        print(self.random_speedlist)
        print(self.random_speedlist[0][1])


        #byr til x marga kassa
        for x in range(number_wall):
            temp=[]
            wall = Player("RTS_Crate.png", playerscale)
            wall.center_x = random.randint(100,2800)
            wall.center_y = random.randint(100,2800)

            temp.extend((wall.center_x,wall.center_y))
            self.wall_pos.append(temp)

            #ætlaði að checka hvort þeir voru inn i hvort öðrum en þetta lætur koðan crasha
            #tok það i burtu en þetta er svippað en checkar bara einu sinni þannig hann getur spawnað í öðrum ef í fyrsta skiptið hann er í einhverjum
            for x in self.wall_pos:
                   for num in range(10):
                       if x[0]-num == wall.center_x-num or x[0]+num == wall.center_x+num:
                           wall.center_x = random.randint(100, 2800)
                       else:
                           break
                       if x[1]-num == wall.center_y - num or x[1]+num == wall.center_y + num:
                           wall.center_y = random.randint(100, 2800)
                       else:
                           break

            self.wall_list.append(wall)

        self.wall=self.wall_list[0]
        print(self.wall_list[1-1])

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        for x in range(7):
            self.box_onbox= arcade.PhysicsEngineSimple(self.wall_list[x-1], self.wall_list)


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

        #arcade.draw_text(f"pos : x {self.pos_player_X}: y {self.pos_player_Y}",self.pos_player_X-150, self.pos_player_Y+150, arcade.color.WHITE, 24)
        #score
        arcade.draw_text(f"score: {self.score}", self.pos_player_X - 60,self.pos_player_Y + 150, arcade.color.WHITE, 24)

        #timer
        arcade.draw_text(f"timi: {self.timi:.2f}", self.pos_player_X +450, self.pos_player_Y + 400,arcade.color.WHITE, 20)

        #teikar ef þu ert komin með 10 score og fer ef ytt er a E/e
        if self.textgoawayunlock==True:
            arcade.draw_text(f"unlock wepon 2 by pressing E/e", self.pos_player_X - 650, self.pos_player_Y -400, arcade.color.WHITE,14)


        if self.wpn==1:
            # vopn 1 ytta a
            arcade.draw_text(f"wepon 1: Bomb", self.pos_player_X - 650, self.pos_player_Y + 400, arcade.color.WHITE,20)
            arcade.draw_text(f"wepon 2: laser", self.pos_player_X - 450, self.pos_player_Y + 400, arcade.color.LIGHT_GRAY,16)
        if self.wpn==2:
            # vopn 2 ytta a
            arcade.draw_text(f"wepon 2: laser", self.pos_player_X - 450, self.pos_player_Y + 400, arcade.color.WHITE,20)
            arcade.draw_text(f"wepon 1: Bomb", self.pos_player_X - 650, self.pos_player_Y + 400, arcade.color.WHITE, 16)

        #camera
        self.camera_for_gui.use()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        self.box_onbox.update()


        self.timi_heild += 1

        self.timi = self.timi_heild / 60

        #start box test


        for x in range(len(self.wall_list)):
            self.timi_local+=1


            if self.timi_local==180:
                self.random_speedlist[x][0]= random.randint(-2, 2)
                self.random_speedlist[x][1] = random.randint(-2, 2)

                self.timi_local = 0

            if self.timi_local!=0:
                self.wall_list[x].center_x += self.random_speedlist[x][0]
                self.wall_list[x].center_y += self.random_speedlist[x][1]

            if self.wall_list[x].center_x< 0+40:
               self.wall_list[x].center_x = 0+40
            if self.wall_list[x].center_x> 3000 - 40:
               self.wall_list[x].center_x = 3000 - 40
            #
            if self.wall_list[x].center_y< 0+40:
                self.wall_list[x].center_y= 0+40
            if self.wall_list[x].center_y> 3000 - 40:
                self.wall_list[x].center_y= 3000 - 40

        #end box test



        self.timi_heild+=1
        self.timi=self.timi_heild/60

        self.bomb_list.update()
        for bomb in self.bomb_list:
            pass

        #self.scroll_to_player()
        self.pos_player_X=self.player_sprite.center_x
        self.pos_player_Y=self.player_sprite.center_y
        #print(self.pos_player_X)

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
                self.score += 1

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


        if key == arcade.key.KEY_1:
            self.wpn=1

        if self.unlock2==True:
            if key == arcade.key.KEY_2:
                self.wpn=2



        if self.score>=10:
            if self.ecnt<1:
                self.textgoawayunlock=True
            if key == arcade.key.E:
                self.ecnt+=1
                self.unlock2=True
                self.textgoawayunlock=False

        #bomb
        if self.wpn==1:
            if key==arcade.key.SPACE:
                bomb = arcade.Sprite("1200px-AA-3-Anab.png",bombsprite)
                # settur skotið þar sem player er
                start_x = self.pos_player_X-15
                start_y = self.pos_player_Y-20
                bomb.change_y = -30
                bomb.angle=90
                bomb.center_x = start_x
                bomb.center_y = start_y
                self.bomb_list.append(bomb)

        if self.unlock2==True:
            if self.wpn == 2:
                if key==arcade.key.SPACE:
                    for x in range(2):
                        bomb = arcade.Sprite("1200px-AA-3-Anab.png", bombsprite)
                        # settur skotið þar sem player er
                        start_x = self.pos_player_X - 15
                        start_y = self.pos_player_Y - 20

                        bomb.change_y = -15+self.shot_y

                        bomb.angle = 90+self.shot_rotate

                        bomb.center_x = start_x
                        bomb.center_y = start_y
                        self.bomb_list.append(bomb)

                        self.shot_rotate+=180
                        self.shot_y +=30
                    self.shot_y =0
                    self.shot_rotate = 0

                    for x in range(2):
                        bomb = arcade.Sprite("1200px-AA-3-Anab.png", bombsprite)
                        # settur skotið þar sem player er
                        start_x = self.pos_player_X - 15
                        start_y = self.pos_player_Y - 20

                        bomb.change_x = -15+self.shot_x

                        bomb.angle = 0 + self.shot_rotate

                        bomb.center_x = start_x
                        bomb.center_y = start_y
                        self.bomb_list.append(bomb)

                        self.shot_rotate += 180
                        self.shot_x+=30
                    self.shot_x =0
                    self.shot_rotate=0


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