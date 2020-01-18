#coding:utf-8
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *
import profile_toolbox
from profile_toolbox import *
import numpy as np
def close_Shear_center_x(profile_constant,cos_value = [],Shear_ST=[],thickness = [], \
						basic_point = [0,0]):
	'''
	Attention that if without the Shear flow, the profile's Ixy must equal to ZERO 
	The Shear Flow used here is still the open-profile Shear Flow, NOT closed one.
	'''

	PSx = 0
	Sxt = 0
	Dst = 0
	x1 = 0
	x2 = 0
	x3 = 0

	mcos_value = cos_value

	if mcos_value == []:
		mcos_value = copy.copy(profile_constant.cos_value)

	if thickness == []:
		if len(mcos_value) == 2:
			thickness = [1]
		else:
			thickness = np.ones(len(mcos_value)-1)
			thickness = thickness.tolist()

	


	A= open_profile.Surround_Area(mcos_value , basic_point)

	x_center = 0
	Sx = profile_constant.Sx
	Ix = profile_constant.Ix
	Shear_flow = Shear_ST


	k = profile_toolbox.if_clockwise(mcos_value)

	if k < 0:
		pass
	if k > 0:
		mcos_value.reverse()
		Shear_flow.reverse()
		thickness.reverse()
		# print('---xxx-----reverse---xxx---in line-')

	if Shear_flow:

		for i in range(0,len(Shear_flow)):
			ys = mcos_value[i][1]
			ye = mcos_value[i+1][1]
			xs = mcos_value[i][0]
			xe = mcos_value[i+1][0]

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)
			P_distance = dot_distance_line(mcos_value[i],mcos_value[i+1],basic_point)

			qpds = Shear_flow[i] * P_distance 
			x1  = x1 + syp.integrate(qpds,(s,0,length))
 
			qtds = Shear_flow[i] / thickness[i] * 1.0
			x2  = x2 + syp.integrate(qtds,(s,0,length))

			tt = 1.0/thickness[i]
			x3 = x3 + syp.integrate(tt,(s,0,length))

		# print('x1,x2,x3',x1,'   ',x2,'   ',x3)
		x_center = x1 - 2*A * x2 / x3
		return x_center

	else:
		for i in range(0,len(Sx)):
			ys = cos_value[i][1]
			ye = cos_value[i+1][1]
			xs = cos_value[i][0]
			xe = cos_value[i+1][0]

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)

			P_distance = dot_distance_line(cos_value[i],cos_value[i+1],basic_point)

			x1 = P_distance * Sx[i]
			PSx  = PSx + syp.integrate(x1,(s,0,length))

			x2 = Sx[i] / thickness[i] * 1.0
			Sxt = Sxt + syp.integrate(x2,(s,0,length))

			x3 = 1.0/thickness[i]
			Dst = Dst + syp.integrate(x3,(s,0,length))

		x_center = (Psx - 2 * A * Sxt / Dst) / Ix
		return x_center


def close_Shear_center_y(profile_constant,cos_value = [],Shear_ST=[],thickness = [], \
						basic_point = [0,0]):

	'''
	Attention that if without the Shear flow, the profile's Ixy must equal to ZERO 
	The Shear Flow used here is still the open-profile Shear Flow, NOT closed one.
	'''

	PSy = 0
	Syt = 0
	Dst = 0
	y1 = 0
	y2 = 0
	y3 = 0

	mcos_value = cos_value

	if mcos_value == []:
		mcos_value = profile_constant.cos_value

	if thickness == []:
		if len(mcos_value) == 2:
			thickness = [1]
		else:
			thickness = np.ones(len(mcos_value)-1)
			thickness = thickness.tolist()

	
	A= open_profile.Surround_Area(mcos_value , basic_point)

	y_center = 0
	Sy = profile_constant.Sy
	Iy = profile_constant.Iy
	Shear_flow = Shear_ST

	# print(Shear_flow)
	k = profile_toolbox.if_clockwise(mcos_value)

	if k < 0:
		mcos_value.reverse()
		Shear_flow.reverse()
		# print('--yyy------reverse----yyy---in_line-')
		# print(mcos_value,'\n',Shear_flow)

	if k > 0:
		pass

	if Shear_flow:
		for i in range(0,len(Shear_flow)):
			ys = mcos_value[i][1]
			ye = mcos_value[i+1][1]
			xs = mcos_value[i][0]
			xe = mcos_value[i+1][0]

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)
			P_distance = dot_distance_line(mcos_value[i],mcos_value[i+1],basic_point)

			qpds = Shear_flow[i] * P_distance 
			y1  = y1 + syp.integrate(qpds,(s,0,length))

			qtds = Shear_flow[i] / thickness[i] * 1.0
			y2  = y2 + syp.integrate(qtds,(s,0,length))

			tt = 1.0/thickness[i]
			y3 = y3 + syp.integrate(tt,(s,0,length))

		y_center = 2*A * y2 / y3 - y1
		return -1*y_center

	else:
		for i in range(0,len(Sy)):
			ys = cos_value[i][1]
			ye = cos_value[i+1][1]
			xs = cos_value[i][0]
			xe = cos_value[i+1][0]

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)

			P_distance = dot_distance_line(cos_value[i],cos_value[i+1],basic_point)

			y1 = P_distance * Sy[i]
			PSy  = PSy + syp.integrate(y1,(s,0,length))

			y2 = Sy[i] / thickness[i] * 1.0
			Syt = Syt + syp.integrate(y2,(s,0,length))

			y3 = 1.0/thickness[i]
			Dst = Dst + syp.integrate(y3,(s,0,length))

		y_center = (2 * A * PSy / Dst - PSy) / Iy
		
		return y_center

###################################################################################

def close_Shear_center(cos_value, profile_constant,thickness = [],basic_point = [0,0]):
	'''
	Only used when the profile with only one closed cell
	'''
	bp = basic_point
	if not is_point_in(bp, cos_value):
		raise 'basic point not in profile,Choose another one'

	Pc = profile_constant

	c_x = copy.copy(cos_value)
	Tk1 = copy.copy(thickness)

	k   = profile_toolbox.if_clockwise(c_x)
	if k > 0:
		c_x.reverse()
		Tk1.reverse()

	cc = open_profile.Open_Profile(c_x,Pc,thickness = Tk1,Qx = 0,Qy = 1)
	xx = close_Shear_center_x(cc,cos_value=c_x,Shear_ST = cc.Shear_ST,\
		thickness = Tk1,basic_point = bp)
##--------------------------------------------------------------------------##

	c_y = copy.copy(cos_value)
	Tk2 = copy.copy(thickness)

	k   = profile_toolbox.if_clockwise(c_y)
	if k < 0:
		c_y.reverse()
		Tk2.reverse()

	dd = open_profile.Open_Profile(c_y,Pc,thickness = Tk2 ,Qx = 1,Qy = 0)

	yy = close_Shear_center_y(dd,cos_value = c_y,Shear_ST = dd.Shear_ST,\
				thickness = Tk2,basic_point = bp)

	aa = (xx + basic_point[0]).round(4)
	bb = (yy + basic_point[1]).round(4)
	return [ aa , bb]


##################################################################################
#	   / Q(p)
# Qp = |----- ds
#      / G t 
##################################################################################

def get_mutiCloseCells_Qp(dir,shearflow_package,num_list=[],thickness=[],G = {}):

	if num_list ==[]:
		gcos = shearflow_package.keys()
		
	else:
		gcos = line_value_package(num_list)

	print(gcos)
	qgtds = 0

	if thickness == []:
		if len(shearflow_package) == 1:
			thickness = [1]
		elif len(shearflow_package) > 1:
			thickness = 1*np.ones(len(shearflow_package))
			thickness = thickness.tolist()

	if G == {}:
		for (v ,j)  in shearflow_package:
	 		G[(v ,j )] = 1.0

	for i in range(0,len(gcos)):

		if (gcos[i][0] , gcos[i][1]) in shearflow_package.keys():
			dot1 = dir[gcos[i][0]]
			dot2 = dir[gcos[i][1]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)
			theta = math.atan2(yy, xx)

			Da = shearflow_package[(gcos[i][0] , gcos[i][1])] / (G[(gcos[i][0] , gcos[i][1])]*thickness[i])
			
			# Da = shearflow_package[(gcos[i][0] , gcos[i][1])] / G[i] 
			
			qgtds  = qgtds + syp.integrate(Da,(s,0,length)) 


		elif (gcos[i][1] , gcos[i][0]) in shearflow_package.keys():

			dot1 = dir[gcos[i][0]]
			dot2 = dir[gcos[i][1]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)

			yq = shearflow_package[(gcos[i][1] , gcos[i][0])] / \
					G[(gcos[i][1] , gcos[i][0])] /thickness[i]

			qgtds  = qgtds + syp.integrate(yq,(s,0,length)) * -1
		
		else:
			raise 'No Flow in the package'
	return qgtds


##################################################################################
#	   /  1
# Qp = |----- ds
#      / G t 
##################################################################################
def get_mutiCloseCells_Gt(dir,shearflow_package,num_list=[],thickness=[],G = {}):

	if num_list ==[]:
		gcos = shearflow_package.keys()
		
	else:
		gcos = line_value_package(num_list)

	qgtds = 0

	if thickness == []:
		if len(shearflow_package) == 1:
			thickness = [1]
		elif len(shearflow_package) > 1:
			thickness = 1*np.ones(len(shearflow_package))
			thickness = thickness.tolist()

	if G == {}:
		for (v ,j)  in shearflow_package:
	 		G[(v ,j )] = 1.0

	for i in range(0,len(gcos)):

		if (gcos[i][0] , gcos[i][1]) in shearflow_package.keys():
			dot1 = dir[gcos[i][0]]
			dot2 = dir[gcos[i][1]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)
			theta = math.atan2(yy, xx)

			Da = 1.0/ (G[(gcos[i][0] , gcos[i][1])]*thickness[i])
				 		
			qgtds  = qgtds + syp.integrate(Da,(s,0,length)) 


		elif (gcos[i][1] , gcos[i][0]) in shearflow_package.keys():

			dot1 = dir[gcos[i][0]]
			dot2 = dir[gcos[i][1]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)

			yq = 1.0 / G[(gcos[i][1] , gcos[i][0])] /thickness[i]

			qgtds  = qgtds + syp.integrate(yq,(s,0,length))  
		
		else:
			raise 'No Flow in the package'
	return qgtds

# def get_mutiCloseCells_Gt(dir,num_list=[],thickness=[],G = {}):

# 	gcos = line_value_package(num_list)

# 	qt = 0

# 	if thickness == []:
# 		if len(num_list) == 1:
# 			thickness = [1]
# 		elif len(num_list) > 1:
# 			thickness = 1*np.ones(len(num_list))
# 			thickness = thickness.tolist()

# 	# if G == []:
# 	# 	if len(num_list) == 1:
# 	# 		G = [1]
# 	# 	elif len(num_list) > 1:
# 	# 		G = 1*np.ones(len(num_list))
# 	# 		G = G.tolist()
# 	if G == {}:
# 		for (v ,j)  in shearflow_package:
# 	 		G[(v ,j )] = 1.0

# 	for i in range(0,len(gcos)):

# 			dot1 = dir[gcos[i][0]]
# 			dot2 = dir[gcos[i][1]]

# 			xs = dot1[0] ; ys = dot1[1]
# 			xe = dot2[0] ; ye = dot2[1]	

# 			yy = ye - ys
# 			xx = xe - xs
# 			length = math.sqrt(yy**2+xx**2)


# 			yq = 1.0 / G[i] / thickness[i]
#  			qt  = qt + syp.integrate(yq,(s,0,length))

#  	return qt

 
###################################################################################
def get_mutiCloseCells_Moment(dir,shearflow_package,num_list=[],basic_point = [0,0]):

	if num_list ==[]:
		gcos = shearflow_package.keys()

		# if not is_point_in(basic_point, dir.values()):
		# 	raise 'basic point not in profile,Choose another one'
		
	else:
		gcos = line_value_package(num_list)

		if not is_point_in(basic_point,[dir[n] for n in num_list]):
			raise 'basic point not in profile,Choose another one'

	moment = 0

	for i in range(0,len(gcos)):

		if (gcos[i][0] , gcos[i][1]) in shearflow_package.keys():
			dot1 = dir[gcos[i][0]]
			dot2 = dir[gcos[i][1]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)

			# print(length)

			P_distance = dot_distance_line(dot1 , dot2 ,basic_point)

			LR = letf_or_right(dot1 , dot2 ,basic_point)

			Da = shearflow_package[(gcos[i][0] , gcos[i][1])] * P_distance
	
			moment  = moment + syp.integrate(Da,(s,0,length)) * LR


		elif (gcos[i][1] , gcos[i][0]) in shearflow_package.keys():

			dot1 = dir[gcos[i][1]]
			dot2 = dir[gcos[i][0]]

			xs = dot1[0] ; ys = dot1[1]
			xe = dot2[0] ; ye = dot2[1]	

			yy = ye - ys
			xx = xe - xs
			length = math.sqrt(yy**2+xx**2)


			P_distance = dot_distance_line(dot1 , dot2 ,basic_point)

			LR = letf_or_right(dot1 , dot2 ,basic_point)

			Da = shearflow_package[(gcos[i][1] , gcos[i][0])] * P_distance 
	
			moment  = moment + syp.integrate(Da,(s,0,length)) * LR

		else:
			raise 'No Flow in the package'

	return moment

###################################################################################
def get_resultant_Q(dir,shearflow_package):
	Q = 0
	Qx = 0
	Qy = 0

	gcos = shearflow_package.keys()

	for i in range(len(gcos)):

		dot1 = dir[gcos[i][0]]
		dot2 = dir[gcos[i][1]]

		xs = dot1[0] ; ys = dot1[1]
		xe = dot2[0] ; ye = dot2[1]	

		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)
		theta = math.atan2(yy, xx)

		Da = shearflow_package[(gcos[i][0] , gcos[i][1])]

		Q  = syp.integrate(Da,(s,0,length))

		Qxx = Q * math.cos(theta)
		Qyy = Q * math.sin(theta)

		Qx = Qx + Qxx
		Qy = Qy + Qyy

	return {'Qx':Qx,'Qy':Qy}

######################################################################################################################################

def solve_Qn(area = [], Gt = [],Qp = []):
	num = len(area)+1
	area.append(0)
	area1 = [-1*n for n in area]

	matrix1 = np.zeros((num,num))

	if num == 3:

		matrix1[0,0] = Gt[0][0] ; matrix1[0,1] = -Gt[0][1]
		matrix1[1,0] = -Gt[1][0] ; matrix1[1,1] = Gt[1][1]

	elif num > 3:
		matrix1[0,0] = Gt[0][0] ; matrix1[0,1] = -Gt[0][1]
		matrix1[num-2,-3] = -Gt[-1][0] ; matrix1[num-2,num-2] = Gt[-1][1]

		for i in range(1,num-2):
			matrix1[i,i-1] = -Gt[i][0]
			matrix1[i,i]   =  Gt[i][1]
			matrix1[i,i+1] = -Gt[i][2]

	matrix1[:,-1] = np.matrix(area1)
	matrix1[-1,:] = np.matrix(area)

	Qpp = [-1*n for n in Qp]
	QQpp = np.matrix(Qpp)
	matrix1 = np.mat(matrix1)

	a = matrix1.I * QQpp.T
	# print(matrix1)
	# print(QQpp.T)
	return a

######################################################################################################################################

def get_mutiCloseCells_ShearCenter(area = [], Gt = [],Qp = [],Q = 1):
	num = len(area)+1
	area.append(-Q)

	matrix1 = np.zeros((num,num))

	if num == 3:

		matrix1[0,0] = Gt[0][0] ; matrix1[0,1] = -Gt[0][1]
		matrix1[1,0] = -Gt[1][0] ; matrix1[1,1] = Gt[1][1]

	elif num > 3:
		matrix1[0,0] = Gt[0][0] ; matrix1[0,1] = -Gt[0][1]
		matrix1[num-2,-3] = -Gt[-1][0] ; matrix1[num-2,num-2] = Gt[-1][1]

		for i in range(1,num-2):
			matrix1[i,i-1] = -Gt[i][0]
			matrix1[i,i]   =  Gt[i][1]
			matrix1[i,i+1] = -Gt[i][2]

	matrix1[-1,:] = np.matrix(area)

	Qpp = [-1*n for n in Qp]
	QQpp = np.matrix(Qpp)
	matrix1 = np.mat(matrix1)

	
	# print(matrix1)
	# print(QQpp.T)
	a = matrix1.I * QQpp.T
	return a

######################################################################################################################################
def update_mutiCloseCells_Shearflow(shearflow_package,num_list=[],Q0 = 0):
	if num_list ==[]:
		gcos = shearflow_package.keys()
		
	else:
		gcos = line_value_package(num_list)

	new_pak = copy.copy(shearflow_package)
	for i in range(0,len(gcos)):

		if (gcos[i][0] , gcos[i][1]) in shearflow_package.keys():

			new_pak[(gcos[i][0] , gcos[i][1])] = \
						shearflow_package[(gcos[i][0] , gcos[i][1])] + Q0

		elif (gcos[i][1] , gcos[i][0]) in shearflow_package.keys():

			 new_pak[(gcos[i][1] , gcos[i][0])] = \
						shearflow_package[(gcos[i][1] , gcos[i][0])] + Q0

		else:
			raise 'No Flow in the package'
	return new_pak

if __name__ == "__main__":
	solve_Qn(area=[1,2],Gt = [[11,12],[12,22]],Qp = [2,1,0])

	print(solve_Qn(area=[1,2,3],Gt = [[11,12],[12,22,23],[23,33]],Qp = [3,2,1,0]))

	print(get_mutiCloseCells_ShearCenter(area=[1,2,3],Gt = [[11,12],[12,22,23],[23,33]],Qp = [3,2,1,0]))