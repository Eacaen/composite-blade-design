import read_exe
from profile import *
import numpy as np
import scipy as sp
import sympy as syp
import math
import copy
import profile_toolbox
from profile_toolbox import *
t = syp.symbols('t')
c = syp.symbols('c')
x = syp.symbols('x')
y = syp.symbols('y')
s = syp.symbols('s')
Qx= syp.symbols('Qx')
Qy= syp.symbols('Qy')


#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
class Open_Profile(object):
	"""
	docstring for Open_Profile
	accept the profile constant and 
	only the coordinate value [...] to calculate the shear flow
	use this class after the profile has been moved to its centroid
	"""
	def __init__(self,cos_value, profile_constant,thickness = []\
						,Qx = 0,Qy = 1,Mz = 0,Load=[]):
		super(Open_Profile, self).__init__()

		# self.cos_value = cos_value
		self.cos_value = copy.copy(cos_value)
		self.thickness = thickness

		if self.thickness == []:
			if len(self.cos_value) == 2:
				self.thickness = [t]
			elif len(self.cos_value) > 2:
				self.thickness = t*np.ones(len(self.cos_value)-1)
				self.thickness = self.thickness.tolist()

		self.Qx = Qx
		self.Qy = Qy
		self.Mz = Mz

		if Load:
			try:
				self.Qx = Load[0]
 			except:
				self.Qx = 0
			try:
				self.Qy = Load[1]
 			except:
				self.Qy = 0
			try:
				self.Mz = Load[2]
 			except:
				self.Mz = 0

		self.length = []
		self.theta  = []

		# self.length = profile_constant.length
		# self.theta = profile_constant.theta


		for i in range(0,len(self.cos_value)-1):
			yy = self.cos_value[i+1][1] - self.cos_value[i][1]
			xx = self.cos_value[i+1][0] - self.cos_value[i][0]
			self.length.append( math.sqrt(yy**2+xx**2) )
			self.theta.append( math.atan2(yy,xx) )


		self.Ix = profile_constant.Ix
		self.Iy = profile_constant.Iy
		self.Ixy = profile_constant.Ixy

		self.Sx = self.get_Sx()
		self.Sy = self.get_Sy()

		self.Shear_ST = self.get_Shear_ST()
		self.SF_package = self.get_SF_package()
############################################################
#  		  /        /
#    Sx  =| y*dA = |y*t ds 
#         /        /
############################################################
	def get_Sx(self):
		Sx = 0
		Sx_list = []
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)
		 	Sx = (y1*s + (y2-y1)/(2.0*length)*s*s)*t
		 	Sx_list.append(Sx.subs(t,self.thickness[i]))

		for i in range(1,len(Sx_list)):
			Sx_list[i] = Sx_list[i] + Sx_list[i-1].subs(s,self.length[i-1])

		return Sx_list

############################################################
#  		  /        /
#    Sy  =| x*dA = |x*t ds 
#         /        /
############################################################
	def get_Sy(self):

		Sy = 0
		Sy_list = []
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)
		 	Sy = (x1*s + (x2-x1)/(2.0*length)*s*s)*t
		 	Sy_list.append(Sy.subs(t,self.thickness[i]))

		for i in range(1,len(Sy_list)):
			Sy_list[i] = Sy_list[i] + Sy_list[i-1].subs(s,self.length[i-1])

		return Sy_list

	def get_Sx(self):
		Sx = 0
		Sx_list = []
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)
		 	Sx = (y1*s + (y2-y1)/(2.0*length)*s*s)*t
		 	Sx_list.append(Sx.subs(t,self.thickness[i]))

		for i in range(1,len(Sx_list)):
			Sx_list[i] = Sx_list[i] + Sx_list[i-1].subs(s,self.length[i-1])

		return Sx_list
############################################################
#  		  / QxIx - QyIxy \      / QyIy - QxIxy \
#    q = -| -------------| Sy - |--------------| Sx
#         \ IxIy - Ixy**2/      \ IxIy - Ixy**2/
############################################################
	def get_Shear_ST(self):

		shear_st = []
		Qx_bar = (Qx*self.Ix - Qy*self.Ixy)/(self.Ix*self.Iy - self.Ixy**2)
		Qy_bar = (Qy*self.Iy - Qx*self.Ixy)/(self.Ix*self.Iy - self.Ixy**2)

		for i in range(0,len(self.Sx)):
			q = -Qx_bar*self.Sy[i] - Qy_bar*self.Sx[i]
			# q = Qx_bar*self.Sy[i] + Qy_bar*self.Sx[i]

			q =  q.subs([(Qx,self.Qx),(Qy,self.Qy),(t,self.thickness[i])])
			shear_st.append(q)

		return shear_st

###############################################################################
# package the shear flow in a dictionary
###############################################################################
	def get_SF_package(self):
		from collections import OrderedDict
		sf_pack = OrderedDict()
		if self.Shear_ST:
			for i in range(len(self.Shear_ST)):
				ccos = ( tuple(self.cos_value[i]) , tuple(self.cos_value[i+1]) )
				sf_pack[ccos] = self.Shear_ST[i]
		return sf_pack

###############################################################################

	def report(self):

		print '__doc__-->',self.__doc__
		print 'cos_value-->',self.cos_value
		print 'length-->',self.length
		print 'Ix-->',self.Ix
		print 'Iy-->',self.Iy
		print 'Ixy-->',self.Ixy
		print 'Sx-->',self.Sx
		print 'Sy-->-->',self.Sy
		print 'Shear_ST-->',self.Shear_ST


#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#




############################################################
#  		  /l       /l 
#    Sa  =| p*ds = |  dot_To_line * ds 
#         /0       /0
############################################################
def Surround_Area(cos_value,basic_point = [0,0] ):
	Sa = 0
	Sa_list = []
	for i in range(0,len(cos_value)-1):
		ys = cos_value[i][1]
		ye = cos_value[i+1][1]
		xs = cos_value[i][0]
		xe = cos_value[i+1][0]

		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)

		distance = dot_distance_line(cos_value[i],cos_value[i+1],basic_point)

		Da = distance 
		Sa = Sa + syp.integrate(Da,(s,0,length))

	return Sa/2.0


############################################################
#  		  /             
#    Q0  =| Qs*p*ds  
#         /             
############################################################
def get_Shear_Qo(Shear_ST ,cos_value,Mz = 0,basic_point = [0,0]):
	Q = 0

	for i in range(0,len(Shear_ST)):
		ys = cos_value[i][1]
		ye = cos_value[i+1][1]
		xs = cos_value[i][0]
		xe = cos_value[i+1][0]

		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)

		P_distance = dot_distance_line(cos_value[i],cos_value[i+1],basic_point)

		Da = P_distance * Shear_ST[i]
		Q  = Q + syp.integrate(Da,(s,0,length))

	return Mz - Q

############################################################
#  _   _1_ / 
#  x =  Ix |Sx p ds 
#          /
#-----------------------------------------------------------

def get_Shear_center_x(profile_constant,cos_value = [],Shear_ST=[],basic_point = [0,0]):
	'''
	If the Ixy do not equal to 0,
	MUST use the shear flow to calculate
	'''
	x = 0
	Sx = profile_constant.Sx
	Ix = profile_constant.Ix
	update = 0

	Shear_flow = Shear_ST

	mcos_value = cos_value

	if mcos_value == []:
		mcos_value = profile_constant.cos_value

	k = profile_toolbox.if_clockwise(mcos_value)

	if k < 0:
		pass
	if k > 0:
		mcos_value.reverse()
		Shear_flow.reverse()
		update = 1
 
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
			Da = Shear_flow[i] * P_distance 
			x  = x + syp.integrate(Da,(s,0,length))
 
		return x
##############################################################################3
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
 			Da = P_distance * Sx[i]
 	
 			x  = x + syp.integrate(Da,(s,0,length))

			# print 'x--]]',Sx[i],'dis--]]',P_distance ,'[][][]',syp.integrate(Da,(s,0,length))

		return x / Ix 
#----------------------------------------------------------
#  _   _1_ / 
#  y =  Iy |Sy p ds 
#          /
############################################################
def get_Shear_center_y(profile_constant,cos_value = [],Shear_ST=[],basic_point = [0,0]):
	y = 0
	Sy = profile_constant.Sy
	Iy = profile_constant.Iy

	update = 0

	Shear_flow = Shear_ST

	mcos_value = cos_value

	if mcos_value == []:
		mcos_value = profile_constant.cos_value

	k = profile_toolbox.if_clockwise(mcos_value)

	if k > 0:
		pass
	if k < 0:
		mcos_value.reverse()
		Shear_flow.reverse()
		update = 1
 
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
			Da = Shear_flow[i] * P_distance 
			y  = y + syp.integrate(Da,(s,0,length))
 
		return y

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
			Da = P_distance * Sy[i]
			y  = y + syp.integrate(Da,(s,0,length))
		return y / Iy * -1.0


###################################################################################

def get_Shear_center(cos_value, profile_constant,thickness = [],basic_point = [0,0]):
	
	bp = basic_point

	if not is_point_in(bp, cos_value):
		raise 'basic point not in profile,Choose another one'

	Tk = thickness
	Pc = profile_constant

	c_x = copy.copy(cos_value)
	k   = profile_toolbox.if_clockwise(c_x)
	if k > 0:
		c_x.reverse()
 	cc = Open_Profile(c_x,Pc,thickness = Tk,Qx = 0,Qy = 1)
	xx = get_Shear_center_x(cc,Shear_ST = cc.Shear_ST,basic_point = bp)
 
##--------------------------------------------------------------------------##

 	c_y = copy.copy(cos_value)
	k   = profile_toolbox.if_clockwise(c_y)
	if k < 0:
		c_y.reverse()

	dd = Open_Profile(c_y,Pc,thickness = Tk,Qx =1,Qy = 0)
	yy = get_Shear_center_y(dd,Shear_ST = dd.Shear_ST,basic_point = bp)
	
 	aa = (xx + basic_point[0]).round(4)
 	bb = (yy + basic_point[1]).round(4)
	return [ aa , bb]


###################################################################################
def get_resultant_Q(cos_value = [],Shear_ST=[],thickness = []):
	Q = 0
	Qx = 0
	Qy = 0

	for i in range(len(cos_value)-1):
		xs = cos_value[i][0] ; ys = cos_value[i][1]
		xe = cos_value[i+1][0] ; ye = cos_value[i+1][1]
		
		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)
		theta = math.atan2(yy, xx)

		Da = Shear_ST[i] 
 
		Q  = syp.integrate(Da,(s,0,length))

		Qxx = Q * math.cos(theta)
		Qyy = Q * math.sin(theta)

		Qx = Qx + Qxx
		Qy = Qy + Qyy
		# print '--]]',Shear_ST[i] ,'angle---?',theta*180/3.1415,'------]]  ',Qxx,'    ',Qyy

	return {'Qx':Qx,'Qy':Qy}
###################################################################
def get_resultant_Qx(cos_value = [],Shear_ST=[],thickness = []):
	Q = 0
	Qx = 0

	for i in range(len(cos_value)-1):
		xs = cos_value[i][0] ; ys = cos_value[i][1]
		xe = cos_value[i+1][0] ; ye = cos_value[i+1][1]
		
		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)
		theta = math.atan2(yy, xx)

		Da = Shear_ST[i] 
		Q  = syp.integrate(Da,(s,0,length))
		Qxx = Q * math.cos(theta)

		Qx = Qx + Qxx
		print 'Shear_ST,qxx',Shear_ST[i],'----]',Qxx
	return Qx

###################################################################
def get_resultant_Qy(cos_value = [],Shear_ST=[],thickness = []):
	Q = 0
	Qy = 0
 
	for i in range(len(cos_value)-1):
		xs = cos_value[i][0] ; ys = cos_value[i][1]
		xe = cos_value[i+1][0] ; ye = cos_value[i+1][1]
		
		yy = ye - ys
		xx = xe - xs
		length = math.sqrt(yy**2+xx**2)
		theta = math.atan2(yy, xx)

		Da = Shear_ST[i] 
		Q  = syp.integrate(Da,(s,0,length))
		Qyy = Q * math.sin(theta)
		Qyyy = too_small(Qyy, 1e-5)
		Qy = Qy + Qyyy
	return Qy

###################################################################
def get_circle(cos_value = [],Shear_ST=[]):
	Q = 0

	for i in range(len(cos_value)-1):
		xs = cos_value[i][0] ; ys = cos_value[i][1]
		xe = cos_value[i+1][0] ; ye = cos_value[i+1][1]
		
		yy = ye - ys
		xx = xe - xs

		length = math.sqrt(yy**2+xx**2)
		Da = Shear_ST[i]

		Q  = syp.integrate(Da,(s,0,length))

		print 'Shear_ST line',i,Q
	# return Q

if __name__ == "__main__":

	# v = read_exe.Read_COS('test3.xlsx')
	# print v.cos_value
	# v.cos_value_findCentroid()
	# xy = v.cos_value
	# tk = v.TK

	# xy = [[-1,-1],[0,-1],[0,1],[-1,1]]

	xy = [[-1,-1],[0,-1],[1,-1],[-1,1],[0,1],[1,1]]
	tk = np.ones(len(xy))
	pro = Profile_Constant(xy,tk)
	print pro.__doc__
	print pro.cos_value
	print pro.Ix
	print pro.Iy
	print pro.Ixy
	print pro.Area
	
	cccc = [[-1,-1],[0,-1],[1,-1],[-1,1]]
	val = Open_Profile(cccc,pro)
	# val.report()
	print val.cos_value,len(val.cos_value),len(val.Sx)
	print val.Shear_ST,len(val.Shear_ST)
	print val.SF_package
 
	# print dot_distance_line([0,0], [0,4], [1,2])
	if 0:
		if val.Shear_ST:
			import matplotlib.pyplot as plt
			import matplotlib

			for n in range(0,len(val.Shear_ST)):
				xl = np.linspace(0,val.length[n],100)
				yl = []
				for i in xl:
					yl.append(val.Shear_ST[n].subs(s,i))
				plt.plot(xl,yl)
			plt.grid()
			plt.show()

