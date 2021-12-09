#easy
#start box test

wall=self.wall_list[0]
if self.movecnt==0:
    self.movecnt+=1
    wall.center_y = 400
    wall.center_x = 400
    print("wewe")

self.timi_local+=1

if self.timi_local==180:
    self.box_x_speed= random.randint(-2, 2)
    self.box_y_speed = random.randint(-2, 2)
    print(self.box_x_speed)
    print(self.box_y_speed)
    print("meow")
    self.timi_local = 0
else:
    wall.center_x += self.box_x_speed
    wall.center_y += self.box_y_speed

if wall.center_x < 0+10:
   wall.center_x = 0
if wall.center_x > 3000 - 10:
   wall.center_x = 3000 - 1
#
if wall.center_y< 0+10:
    wall.center_y= 0
if wall.center_y> 3000 - 10:
    wall.center_y= 3000 - 1

#end box test



#medium

#start box test

wall=self.wall_list[0]
if self.movecnt==0:
    self.movecnt+=1
    wall.center_y = 400
    wall.center_x = 400
    print("wewe")

self.timi_local+=1

if self.timi_local==120:
    self.box_x_speed= random.uniform(-2, 2)
    self.box_y_speed = random.uniform(-2, 2)
    print(self.box_x_speed)
    print(self.box_y_speed)
    print("meow")
    self.timi_local = 0
else:
    wall.center_x += self.box_x_speed
    wall.center_y += self.box_y_speed

if wall.center_x < 0+10:
   wall.center_x = 0
if wall.center_x > 3000 - 10:
   wall.center_x = 3000 - 1
#
if wall.center_y< 0+10:
    wall.center_y= 0
if wall.center_y> 3000 - 10:
    wall.center_y= 3000 - 1

#end box test



#hard

#start box test

wall=self.wall_list[0]
if self.movecnt==0:
    self.movecnt+=1
    wall.center_y = 400
    wall.center_x = 400
    print("wewe")

self.timi_local+=1

if self.timi_local==80:
    self.box_x_speed= random.uniform(-4, 4)
    self.box_y_speed = random.uniform(-4, 4)
    print(self.box_x_speed)
    print(self.box_y_speed)
    print("meow")
    self.timi_local = 0
else:
    wall.center_x += self.box_x_speed
    wall.center_y += self.box_y_speed

if wall.center_x < 0+10:
   wall.center_x = 0
if wall.center_x > 3000 - 10:
   wall.center_x = 3000 - 1
#
if wall.center_y< 0+10:
    wall.center_y= 0
if wall.center_y> 3000 - 10:
    wall.center_y= 3000 - 1

#end box test