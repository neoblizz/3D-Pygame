import pygame
import math
from pygame.locals import *
angle = 0
orgin_y = 0 
orgin_y = 0
clock = 0
gameDisplay = pygame.display.set_mode((1,1))
color = 0



#########################################################
###############    Set up 3D Plane     ##################
#########################################################
def setup(display_Width, display_Height,background_Color):
	pygame.init()
	gameDisplay = pygame.display.set_mode((display_Width,display_Height))
	pygame.display.set_caption('3D vector')
	clock = pygame.time.Clock()
	gameDisplay.fill(background_Color)
	return clock, gameDisplay

#########################################################
############    Initialize Rectangle   ##################
#########################################################
def rect_ini(rect_width, rect_height,rect_depth,rect_x,rect_y,rect_z):
	EDGES = [0,0,0,0,0,0,0,0]
	EDGES[0] = [rect_x+rect_width, rect_y+rect_height, rect_z+rect_depth, 1]
	EDGES[1] = [rect_x+rect_width, rect_y, rect_z+rect_depth, 1]
	EDGES[2] = [rect_x, rect_y, rect_z+rect_depth, 1]
	EDGES[3] = [rect_x, rect_y+rect_height, rect_z+rect_depth, 1]
	EDGES[4] = [rect_x+rect_width, rect_y+rect_height, rect_z, 1]
	EDGES[5] = [rect_x+rect_width, rect_y, rect_z, 1]
	EDGES[6] = [rect_x, rect_y, rect_z, 1]
	EDGES[7] = [rect_x, rect_y+rect_height, rect_z, 1]
	return EDGES

#########################################################
##############    Initialize Trangle   ##################
#########################################################
def tri_ini(tri_data):
	EDGES = [0,0,0,0]
	EDGES[0] = [tri_data[0],tri_data[1],tri_data[2],1]
	EDGES[1] = [tri_data[3],tri_data[4],tri_data[5],1]
	EDGES[2] = [tri_data[6],tri_data[7],tri_data[8],1]
	EDGES[3] = [tri_data[9],tri_data[10],tri_data[11],1]
	return EDGES

#########################################################
####################    Triangle   ######################
#########################################################
def drawTri(EDGES,color):
	drawLine(EDGES[0],EDGES[1],2,color)
	drawLine(EDGES[1],EDGES[2],2,color)
	drawLine(EDGES[2],EDGES[0],2,color)
	drawLine(EDGES[0],EDGES[3],2,color)
	drawLine(EDGES[1],EDGES[3],2,color)
	drawLine(EDGES[2],EDGES[3],2,color)


#########################################################
####################    Rectangle  ######################
#########################################################
def drawRect(EDGES,color):
	drawLine(EDGES[0],EDGES[1],2,color)
	drawLine(EDGES[1],EDGES[2],2,color)
	drawLine(EDGES[2],EDGES[3],2,color)
	drawLine(EDGES[0],EDGES[3],2,color)
	drawLine(EDGES[4],EDGES[5],2,color)
	drawLine(EDGES[5],EDGES[6],2,color)
	drawLine(EDGES[6],EDGES[7],2,color)
	drawLine(EDGES[7],EDGES[4],2,color)
	drawLine(EDGES[0],EDGES[4],2,color)
	drawLine(EDGES[1],EDGES[5],2,color)
	drawLine(EDGES[2],EDGES[6],2,color)
	drawLine(EDGES[3],EDGES[7],2,color)


#########################################################
####################     Line      ######################
#########################################################
def drawLine(EDGE1,EDGE2,width,color):
	x1,y1,z1= xyz(EDGE1[0],EDGE1[1],EDGE1[2])
	x2,y2,z2 = xyz(EDGE2[0],EDGE2[1],EDGE2[2])
	pygame.draw.line(gameDisplay,color,(x1,y1),(x2,y2),width)

########################################################
###################  Match Coordinate ##################
########################################################
def xyz(x,y,z):
	x = x + 0.5 * z * math.cos(angle) + orgin_x
	y = orgin_y - (y + 0.5 * z * math.sin(angle))
	z = 0
	return x,y,z