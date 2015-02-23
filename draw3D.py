import pygame
import math
from pygame.locals import *
import color
angle = 0
orgin_x = 0 
orgin_y = 0
clock = 0
gameDisplay = pygame.display.set_mode((1,1))
color = (0,0,0)
perspective_distortion = 1000
sub_angle = math.pi/30
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

def v_int(tri_data):
	num_v = len(tri_data)/3
	EDGES = [0 for x in range(num_v)]
	i = 0
	for k in range(num_v):
		EDGES[k] = [tri_data[3*k],tri_data[3*k+1],tri_data[3*k+2],1]
	return EDGES

def drawObj(EDGES,index,color,width):
	for k in range(len(index)):
		temp = index[k]
		if len(temp) == 1:
			temp2 = temp[0]
			if temp2 == "black":
				color = (0,0,0)
			elif temp2 == 'skin':
				color = (255,218,185)
			elif temp2 == "white":
				color = (255,255,255)
			elif temp2 == "dkblue_pure":
				color = (25,25,112)
			elif temp2 == "deepgreen":
				color = (0,100,0)
			elif temp2 == "dkgrey":
				color = (105,105,105)
			elif temp2 == "brown":
				color = (139,69,19)
			elif temp2 == "brnhair":
				color = (210,105,30)
			elif temp2 == "fldkred":
				color = (178,34,34)
		elif  len(temp) > 1:
			area = []
			for j in range(0,len(temp)):
				temp3 = temp[j] - 1
				edge = EDGES[temp3]
				area.append(edge)
			points1 = []
			points2 = []
			for k in range(0,len(area)):
				EDGE1 = area[k]
				point1 = xyz(EDGE1[0],EDGE1[1],EDGE1[2],orgin_x_1,orgin_y_1,-1 * sub_angle)
				point2 = xyz(EDGE1[0],EDGE1[1],EDGE1[2],orgin_x_2,orgin_y_2,sub_angle)
				points1.append(point1)
				points2.append(point2)
			pygame.draw.polygon(gameDisplay, color, points1, width)
			pygame.draw.polygon(gameDisplay, color, points2, width)
	return color

########################################################
###################  Match Coordinate ##################
########################################################
def xyz(x,y,z, orgin_x, orgin_y,angle2):
	scale = 50
	x = x * scale
	y = y * scale
	z = z * scale
	x = x + x * z / perspective_distortion
	y = -1 * (y + y * z / perspective_distortion)
	z = z + z / perspective_distortion
	x = x + 0.5 * z * math.cos(angle + angle2) + orgin_x
	y = y + 0.5 * z * math.sin(angle + angle2) + orgin_y
	z = 0
	return x,y

