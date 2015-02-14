def isInsidePo(a,poly):
	x = a[0]
	y = a[1]
	print poly
	print x,y
	n = len(poly)
	inside = False
	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
	return inside



poly = [[1,3],[2,1],[3,2],[2,4]]

max_left = poly[0][0]
max_index = 0
for k in range(1,len(poly)):
	if poly[k][0] > max_left:
		max_left = poly[k][0]
		max_index = k
#print max_index

a = [1,3]
isInside = isInsidePo(a,poly)
if isInside == True:
	print "isInside"


