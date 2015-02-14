
import pygame
import math
import draw3D
import transform
from pygame.locals import *
import color
#########################################################
####################     Setup     ######################
#########################################################
fps = 40
display_Width = 1920   #700
display_Height = 1080  #400
angle = math.pi / 2
rotate_angle = math.pi / 18

# center point: 400, 300 
orgin_x_1 = display_Width/4
orgin_y_1 = display_Height/2
draw3D.orgin_x_1 = orgin_x_1
draw3D.orgin_y_1 = orgin_y_1


orgin_x_2 = display_Width/4 * 3
orgin_y_2 = display_Height/2
draw3D.orgin_x_2 = orgin_x_2
draw3D.orgin_y_2 = orgin_y_2



#########################################################
####################keyboard events######################
#########################################################
def play(EDGES,index,color, width):
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					#EDGES = draw3D.rect_ini(rect_width, rect_height,rect_depth,rect_x,rect_y,rect_z)
					EDGES = draw3D.v_int(numbers)
					angle = math.pi / 2
				if event.key == K_LEFT:
					move_x = -1
				if event.key == K_RIGHT:
					move_x = 1
				if event.key == K_DOWN:
					move_y = -1
				if event.key == K_UP:
					move_y = 1
				if event.key == K_LSHIFT:
					move_z = -1
				if event.key == K_RSHIFT:
					move_z = 1
				if event.key == K_1:
					rotate_dir = 1
				if event.key == K_2:
					rotate_dir = 2
				if event.key == K_3:
					rotate_dir = 3
				if event.key == K_l:
					scale_x = 1.09
					scale_y = 1.09
					scale_z = 1.09
				if event.key == K_s:
					scale_x = 0.95
					scale_y = 0.95
					scale_z = 0.95
				if event.key == K_q:
					draw3D.angle = draw3D.angle +  math.pi /5
				if event.key == K_w:
					draw3D.angle = draw3D.angle -  math.pi /5
			else:
				move_x = 0
				move_y = 0
				move_z = 0
				rotate_dir = 0
				scale_x = 1.0	
				scale_y = 1.0
				scale_z = 1.0

		for i in range(len(EDGES)):
			if rotate_dir != 0:
				EDGES[i] = transform.rotation(EDGES[i],rotate_angle,rotate_dir)
			if move_x != 0 or move_y != 0 or move_z != 0: 
				EDGES[i] = transform.translation(EDGES[i],move_x,move_y,move_z)	
			if scale_x != 1 or scale_y != 1 or scale_z != 1:
				EDGES[i] = transform.scale(EDGES[i],scale_x,scale_y,scale_z)

		gameDisplay.fill((0,0,0))   # clean up screen 
		color = draw3D.drawObj(EDGES,index,color,width)
		pygame.display.update()
		clock.tick(fps)




#########################################################
###############          Main              ##############
#########################################################

# setup 3D enviroment
clock, gameDisplay = draw3D.setup(display_Width, display_Height,color.white)
numbers = []
index = []
colorOn = False     #Turn color on by setting it to true
line_width = 1
with open("people.obj") as f:   #choice "airplane.obj", "people.obj", "boat.obj"
    lines = f.readlines()
for i in range(len(lines)):
	k = lines[i].split(' ', 1)
	if k[0] == 'v': 
		j = k[1]
		numbers = numbers + [float(s) for s in j.split()]
	elif k[0] == 'f':
		h = [int(s) for s in k[1].split()]
		index.append(h)
	elif k[0] == "usemtl" and colorOn == True:
		l = [s for s in k[1].split()]
		index.append(l)

EDGES = draw3D.v_int(numbers)
draw3D.angle = angle
play(EDGES,index,color.white, line_width)
pygame.quit()
quit()