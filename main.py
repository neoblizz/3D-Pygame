
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
display_Width = 800
display_Height = 600
angle = math.pi / 4
rotate_angle = math.pi / 18
# center point: 400, 300
orgin_x = 400
orgin_y = 300
draw3D.orgin_x = orgin_x
draw3D.orgin_y = orgin_y


#########################################################
####################keyboard events######################
#########################################################
def play(EDGES):
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					EDGES = rect_setup(rect_width, rect_height,rect_depth,rect_x,rect_y,rect_z)
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
					scale_x = 1.01	
					scale_y = 1.01
					scale_z = 1.01
				if event.key == K_s:
					scale_x = 0.99
					scale_y = 0.99
					scale_z = 0.99
			else:
				move_x = 0
				move_y = 0
				move_z = 0
				rotate_dir = 0
				scale_x = 1.0	
				scale_y = 1.0
				scale_z = 1.0

		for i in range(len(EDGES)):
			EDGES[i] = transform.rotation(EDGES[i],rotate_angle,rotate_dir)
			EDGES[i] = transform.translation(EDGES[i],move_x,move_y,move_z)	
			EDGES[i] = transform.scale(EDGES[i],scale_x,scale_y,scale_z)
		gameDisplay.fill(color.white)
		draw3D.angle = angle
		draw3D.drawRect(EDGES[:8],color.black)
		draw3D.drawTri(EDGES[8:],color.red)
		pygame.display.update()
		clock.tick(fps)




#########################################################
###############          Main              ##############
#########################################################

# setup 3D enviroment
clock, gameDisplay = draw3D.setup(display_Width, display_Height,color.white)
# given rectangle coordinate 
rect_width = 100
rect_height = 100
rect_depth = 100
rect_x = - 50
rect_y = -50
rect_z = -50

# initialize 3D rectangle, return vertice vectors(8)
EDGES1 = draw3D.rect_ini(rect_width, rect_height,rect_depth,rect_x,rect_y,rect_z)

# initialize 3D triangle, return vertice vectors(4)
tri_data = [0,50,0,0,100,0,50,50,50,50,50,-50]
#tri_data = [50,50,50,50,-50,50,-50,50,50,-50,50,-50]
EDGES2 = draw3D.tri_ini(tri_data) 
EDGES = EDGES1 + EDGES2
play(EDGES)
pygame.quit()
quit()