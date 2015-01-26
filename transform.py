import math

########################################################
###################     Rotation      ##################
########################################################
def rotation(vector,angle, dir):
	a = math.cos(angle)
	b = math.sin(angle)
	X = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	if dir == 1:
		X =  [[1,0,0,0],[0,a,-1*b,0],[0,b,a,0],[0,0,0,1]]
	elif dir == 2:
		X =  [[a,0,b,0],[0,1,0,0],[-1*b,0,a,0],[0,0,0,1]]
	elif dir == 3:
		X = [[a,-1*b,0,0],[b,a,0,0],[0,0,1,0],[0,0,0,1]]
	return matrixMulti(X,vector)

########################################################
###################     translation   ##################
########################################################
def translation(vector,trans_x, trans_y, trans_z):
	X = [[1,0,0,trans_x],[0,1,0,trans_y],[0,0,1,trans_z],[0,0,0,1]]
	return matrixMulti(X,vector)

########################################################
###################     Scale         ##################
########################################################
def scale(vector,scale_x, scale_y, scale_z):
	X = [[scale_x,0,0,0],[0,scale_y,0,0],[0,0,scale_z,0],[0,0,0,1]]
	return matrixMulti(X,vector)


def matrixMulti(X,Y):
	result = [0,0,0,0]
	for i in range(len(X)):
		for j in range(len(Y)):
			result[i] += X[i][j] * Y[j]
	return result