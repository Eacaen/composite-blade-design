#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import sympy as syp
import math
import copy
########################################################################

def dot_distance_line(dot1,dot2,dot0):
	A = dot2[1] - dot1[1]
	B = dot1[0] - dot2[0]
	C = dot2[0]*dot1[1] - dot1[0]*dot2[1]
	dis = abs(A*dot0[0] + B*dot0[1] + C)/math.sqrt(A*A + B*B)
	return dis


########################################################################

def too_small(a,b):
	if abs(a) < b :
		a = 0.00
	else:
		pass

	return a

########################################################################

def if_clockwise(cos = []):
	'''
	(xi - xi-1) * (yi+1 - yi) - (yi - yi-1) * (xi+1 - xi)
	positive Counterclockwise
	negative Clockwise
	'''
	
	a = copy.deepcopy(cos)
	k = int(len(a)) / 2
	xi = a[k-1][0] #i-1
	yi = a[k-1][1]

	xii = a[k][0]  # i
	yii = a[k][1]

	xiii = a[k+1][0]  #i + 1
	yiii = a[k+1][0]

	clock = (xii - xi) * (yiii - yii) - (yii - yi) * (xiii - xii)

	if clock != 0:
		return -1*clock / abs(clock)

	if clock == 0:
		a.remove(a[k])
		return if_clockwise(a)

########################################################################

def is_point_in(point, mcos_value):
	if point in mcos_value:
		return True
		
	cos_value = copy.copy(mcos_value)
	count = 0
	mul = 0
	x = point[0]
	y = point[1]
	x1, y1 = cos_value[0]
	x1_part = (y1 > y) or ((x1 > x) and (y1 == y)) # x1在哪一部分中

	x2, y2 = '', ''  # cos_value[1]
	cos_value.append((x1, y1))
	for point in cos_value[1:]:
		x2, y2 = point
		x2_part = (y2 > y) or ((x2 > x) and (y2 == y)) # x2在哪一部分中
		if x2_part == x1_part:
			x1, y1 = x2, y2
			continue

		mul = (x1 - x)*(y2 - y) - (x2 - x)*(y1 - y)
		if mul > 0:  # 叉积大于0 逆时针
			count += 1

		elif mul < 0:
			count -= 1
 
		elif mul == 0:
			return True

		x1, y1 = x2, y2
		x1_part = x2_part
       	
	if count == 2 or count == -2:
		return True
	else:
		return False

########################################################################
# S > 0 , left
# S < 0 , right
# S = 0 , in the line
########################################################################
def letf_or_right(A , B , C):
	x1 = A[0] ; y1 = A[1]
	x2 = B[0] ; y2 = B[1]
	x3 = C[0] ; y3 = C[1]
	s =  (x1-x3)*(y2-y3)-(y1-y3)*(x2-x3) 
	if s == 0:
		return 0
	else:
		return s / abs(s)

########################################################################
if __name__ == "__main__":
	cos_value = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]

	cos_value = [[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
	a = -1
	b = -1
	'''
	for i in range(20):
		a = a + 0.1
		b = -1
		for j in range(20):
			b = b + 0.1
			pp = [a,b]
			print is_point_in(pp, cos_value)
	'''
	print letf_or_right([0,0], [1,0], [0,-1])
	print letf_or_right([0,0], [-1,0], [0,-1])

	print letf_or_right([0,0], [1,0], [-1,1])