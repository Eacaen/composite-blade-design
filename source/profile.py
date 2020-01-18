import numpy as np
import scipy as sp
import sympy as syp
import math
import copy

t = syp.symbols('t')
c = syp.symbols('c')
x = syp.symbols('x')
y = syp.symbols('y')
z = syp.symbols('z')
s = syp.symbols('s')
#  		  /        /
#    Sx  =| y*dA = |y*t ds 
#         /        /
def profile_Sx(cos_value,thickness=[]):
	Sx = 0
	sum_sx = 0

	if thickness == []:
		if len(cos_value) == 2:
			thickness = [t]
		else:
			thickness = t*np.ones(len(cos_value)-1)
			thickness = thickness.tolist()

	for i in range(0,len(cos_value)-1):
		y1 = cos_value[i][1]
		y2 = cos_value[i+1][1]

		x1 = cos_value[i][0]
		x2 = cos_value[i+1][0]

		yy = y2 - y1
		xx = x2 - x1
		length = math.sqrt(yy**2+xx**2)

		Sx = (y1*s + (y2-y1)/(2*length)*s*s)*t

		sum_sx = sum_sx + Sx.subs([(s,length),(t,thickness[i])])
	
	return sum_sx


#  		  /        /
#    Sy  =| x*dA = |x*t ds 
#         /        /
def profile_Sy(cos_value,thickness=[]):
	Sy = 0
	sum_sy = 0

	if thickness == []:
		if len(cos_value) == 2:
			thickness = [t]
		else:
			thickness = t*np.ones(len(cos_value)-1)
			thickness = thickness.tolist()

	for i in range(0,len(cos_value)-1):
		y1 = cos_value[i][1]
		y2 = cos_value[i+1][1]

		x1 = cos_value[i][0]
		x2 = cos_value[i+1][0]

		yy = y2 - y1
		xx = x2 - x1
		length = math.sqrt(yy**2+xx**2)

		Sy = (x1*s + (x2-x1)/(2*length)*s*s)*t
		# print('thickness[i]',thickness[i])
		sum_sy = sum_sy + Sy.subs([(s,length),(t,thickness[i])])

	return sum_sy

def Find_Centroid(cos_value=[],thickness=[],\
				area = 0 ,graph = None,dir = None):
	Sx = 0
	Sy = 0
	if area == 0 or area == None:
		print( 'MUST HAVE THE AREA\n')
		return 

	if cos_value != [] and graph == None:

		Sx = profile_Sx(cos_value,thickness)
		Sy = profile_Sy(cos_value,thickness)

		centroid_x = Sy / area
		centroid_y = Sx / area

		return [centroid_x , centroid_y]
# In graph

	elif graph != None and dir != None:
		for v in graph:
				
			for e in v.getConnections():
				cos_value =[dir[v.id],dir[e.id]]

				thick_ij = v.getWeight(e)

				thickness = [thick_ij]

				Sx = Sx + profile_Sx(cos_value,thickness) 
				Sy = Sy + profile_Sy(cos_value,thickness) 


		centroid_x = Sy /2.0 / area
		centroid_y = Sx /2.0 / area
		return [centroid_x , centroid_y]

def get_length(cos_value):
	yy =  cos_value[1][1] - cos_value[0][1]
	xx =  cos_value[1][0] - cos_value[0][0]
	return math.sqrt(yy**2+xx**2)
#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
#-------------------------------#START OF CLASS#-------------------------------#
class Profile_Constant(object):
	"""docstring for Profile_Constant"""
	def __init__(self, cos_value=[],thickness=[],graph = None,dir = None,unit = 1):
		super(Profile_Constant, self).__init__()
		self.cos_value = copy.copy(cos_value)
		self.thickness = copy.copy(thickness)

		self.graph =  copy.copy(graph)
		self.dir = copy.copy(dir)

		self.length = []
		self.theta  = []
		self.Area = 0

		self.Ix  = 0
		self.Iy  = 0
		self.Ixy = 0
		self.Sx  = 0
		self.Sy  = 0

		self.centroid_x = 0
		self.centroid_y = 0

		self.gravity_center_x = 0
		self.gravity_center_y = 0
		self.gravity_center = [ ]

		self.perimeter = 0

		self.unit = unit
		self.update_profile() # calculate the engineer constant

#######################################################################
# the length and theta maybe calculate by the line itself when used
#
#######################################################################
		# for i in range(0,len(self.cos_value)-1):
		# 	yy = self.cos_value[i+1][1] - self.cos_value[i][1]
		# 	xx = self.cos_value[i+1][0] - self.cos_value[i][0]
		# 	self.length.append( math.sqrt(yy**2+xx**2) )
		# 	self.theta.append( math.atan2(yy,xx) )

	def SI_unit(self,unit=1):
		if not unit==1:
			self.Area = self.Area*1.0/( unit**2)
			self.Ix   = self.Ix*1.0/( unit**4)
			self.Iy   = self.Iy*1.0/( unit**4)
			self.Ixy  = self.Ixy*1.0/( unit**4)
			self.perimeter = self.perimeter*1.0/( unit)

	def update_profile(self):
		self.Ix  = 0
		self.Iy  = 0
		self.Ixy = 0
		self.Sx  = 0
		self.Sy  = 0
		self.Area = 0
		self.centroid_x = 0
		self.centroid_y = 0

		self.gravity_center_x = 0
		self.gravity_center_y = 0
		self.gravity_center = [ ]

		self.perimeter = 0
#######################################################################
# the Profile in a signal line
#
#######################################################################
		if self.graph == None: #and self.thickness != []:

			if self.thickness == []:
				if len(self.cos_value) == 2:
					self.thickness = [t]
				elif len(self.cos_value) > 2:
					self.thickness = t*np.ones(len(self.cos_value)-1)
					self.thickness = self.thickness.tolist()

	########################################################

			for i in range(0,len(self.cos_value)-1):
				yy = self.cos_value[i+1][1] - self.cos_value[i][1]
				xx = self.cos_value[i+1][0] - self.cos_value[i][0]
				self.length.append( math.sqrt(yy**2+xx**2) )

			self.perimeter = sum(self.length)
			# 	self.theta.append( math.atan2(yy,xx) )

			self.Area = self.get_area(self.thickness)
			self.Ix   = self.get_Ix(self.thickness)
			self.Iy   = self.get_Iy(self.thickness)
			self.Ixy  = self.get_Ixy(self.thickness)

			self.gravity_center = self.get_gravity_center(self.thickness)
			self.gravity_center_x = self.gravity_center[0]
			self.gravity_center_y = self.gravity_center[1]
			# self.centroid_x = self.Sy / self.Area
			# self.centroid_y = self.Sx / self.Area

#######################################################################
# the Profile in graph
#
#######################################################################
		elif self.graph != None:
			ddir = self.dir
			for v in self.graph:
				for e in v.getConnections():
					self.cos_value =[ ddir[v.id],ddir[e.id] ]
					# print(v.id,e.id)
					self.perimeter = self.perimeter + get_length(self.cos_value)

					thick_ij = v.getWeight(e)
					thickness = [thick_ij]

					self.Area = self.Area + self.get_area(thickness)
					self.Ix  = self.Ix  + self.get_Ix(thickness)
					self.Iy  = self.Iy  + self.get_Iy(thickness) 
					self.Ixy = self.Ixy + self.get_Ixy(thickness)

					self.gravity_center = self.get_gravity_center(thickness)
					self.gravity_center_x = self.gravity_center_x + self.gravity_center[0]
					self.gravity_center_y = self.gravity_center_y + self.gravity_center[1]

			self.Area = self.Area/2.0
			self.Ix   = self.Ix/2.0
			self.Iy   = self.Iy/2.0
			self.Ixy  = self.Ixy/2.0
			self.perimeter = self.perimeter/2.0

			self.gravity_center_x = self.gravity_center_x/self.Area/2.0
			self.gravity_center_y = self.gravity_center_y/self.Area/2.0
			self.gravity_center = [self.gravity_center_x , self.gravity_center_y]

		# self.SI_unit()
############################################################
#  		  /
#     A  =| dA 
#         /
############################################################
	def get_area(self,thickness):
		A = 0
		for i in range(0,len(self.cos_value)-1):
			yy = self.cos_value[i+1][1] - self.cos_value[i][1]
			xx = self.cos_value[i+1][0] - self.cos_value[i][0]
			leng = math.sqrt(yy**2+xx**2) 

			A = A + leng * thickness[i]
		return A
############################################################
#  		  /
#    Ixx =| y*y dA 
#         /
############################################################
	def get_Ix(self,thickness):
		Ix = 0
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)

			fun = t*length*(y1**2 + y1 * y2 + y2**2) / 3.0

			Ix = Ix + fun.subs(t,thickness[i])

		return Ix
############################################################
#  		  /
#    Iyy =| x*x dA 
#         /
############################################################

	def get_Iy(self,thickness):
		Iy = 0
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)

			fun = t*length*(x1**2 + x1 * x2 + x2**2) / 3.0
			Iy = Iy + fun.subs(t,thickness[i])

		return Iy
############################################################
#  		  /
#    Ixy =| x*y dA 
#         /
############################################################

	def get_Ixy(self,thickness):
		Ixy = 0
		for i in range(0,len(self.cos_value)-1):
			y1 = self.cos_value[i][1]
			y2 = self.cos_value[i+1][1]
			x1 = self.cos_value[i][0]
			x2 = self.cos_value[i+1][0]

			yy = y2 - y1
			xx = x2 - x1
			length = math.sqrt(yy**2+xx**2)
			fun = length*t*(2*x1*y1 + x1*y2 + x2*y1 + 2*x2*y2)/6.0
			Ixy = Ixy + fun.subs(t,thickness[i])

		return Ixy

############################################################
#  		      sum(x*m)
#     G_x  = ---------
#                 M
############################################################
	def get_gravity_center(self,thickness):
		A = []
		aa = 0
		bb = 0
		for i in range(0,len(self.cos_value)-1):
			yy = self.cos_value[i+1][1] - self.cos_value[i][1]
			xx = self.cos_value[i+1][0] - self.cos_value[i][0]

			mid_x = (self.cos_value[i+1][0] + self.cos_value[i][0]) /2.0
			mid_y = (self.cos_value[i+1][1] + self.cos_value[i][1]) /2.0

			leng = math.sqrt(yy**2+xx**2) 
			
			a = leng * mid_x * thickness[i]
			b = leng * mid_y * thickness[i]

			aa = aa + a
			bb = bb + b
			A = [ aa, bb]
		return A
############################################################
# move the profile to it's centroid
############################################################
	def profile_To_centriod(self):

		[Cx,Cy] = Find_Centroid(cos_value = self.cos_value,thickness = self.thickness,\
				area = self.Area,graph = self.graph ,dir = self.dir)
							 
		self.centroid_x = Cx
		self.centroid_y = Cy

		if self.graph == None:
			for i in range(0,len(self.cos_value)):
				self.cos_value[i][0] = self.cos_value[i][0] - self.centroid_x
				self.cos_value[i][1] = self.cos_value[i][1] - self.centroid_y

			self.update_profile()
			return self.cos_value

		elif self.graph != None:

			ddir = {}
			for i in range(0,len(self.dir)):

				x = self.dir[i][0] - round(self.centroid_x,2)
				y = self.dir[i][1] - round(self.centroid_y,2)
				# print('[x,y]',x,y)
				ddir[i] = [x,y]

			self.dir = {}
			self.dir = ddir

			self.update_profile()
			return ddir

############################################################
# stress sigma_z
#
#
#
############################################################
	def stress_z(self,Mx = 0 , My = 0,Nz = 0,Load=[],unit=1):
 		# self.SI_unit(unit)

		if Load:
			try:
				Mx = Load[0]
			except:
				Mx = 0

			try:
				My = Load[1]
			except:
				My = 0

			try:
				Nz = Load[2]
			except:
				Nz = 0

		a = Mx
		Mx = My
		My = a
		
		Jxy = 1 - (self.Ixy)**2 / (self.Ix * self.Iy)
		Mx_bar = My - Mx * (self.Ixy / self.Ix)
		My_bar = Mx - My * (self.Ixy / self.Iy)

		Mx_bar = Mx_bar / Jxy
		My_bar = My_bar / Jxy

		stress = My_bar / self.Iy * x + Mx_bar / self.Ix * y + Nz / self.Area 

		return stress * unit**2


############################################################
# Main_inertia_axis_Angle
#          2(-Ixy)
# tan2a = ---------   Clockwise positive
#          Ix - Iy
############################################################
	def get_Main_inertia_axis_Angle(self):
		yy = -2.0*self.Ixy 
		xx = self.Ix - self.Iy
		theta = math.atan2(yy,xx) 
		return theta/2.0

############################################################
# Rotate the coordinate value
# / x1 \   / cos  sin  \ / x0 \
# |    | = |           | |    |
# \ y1 /   \ -sin  cos / \ y0 /
############################################################
	def cos_value_rotate(self):
		theta = get_Main_inertia_axis_Angle()
		c = math.cos(theta)
		s = math.sin(theta)
		new_value = []
		for i in range(len(self.cos_value)):

			x0 = self.value[i][0]
			y0 = self.value[i][1]

			x1 = c * x0 + s * y0
			y1 = -1*s*x0 + c*y0

			new_value.append([x1,y1])
			
		return new_value



#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#
#-------------------------------#END OF CLASS#-------------------------------#


	
if __name__ == "__main__":

	# xy = [[-1,-1],[0,-1],[0,1],[-1,1]]
	# xy = [[-1,-1],[0,-1]]
	# xy = [[-1,-1],[0,-1],[1,-1],[-1,1],[0,1],[1,1]]

	# print(profile_Sy)([[2,3],[-1,0]])
	# print(profile_Sy)([[-1,0],[2,3]])
	# print(profile_Sx)([[2,3],[-1,0]])
	# print(profile_Sx)([[-1,0],[2,3]])

	xy = [[-2,-1],[0,-1],[0,1],[-2,1]]

	tk = 1*np.ones(len(xy)-1)
	print( tk)
	val = Profile_Constant(xy,tk)
	print(val.__doc__)
	print(val.cos_value)
	print(val.Ix)
	print(val.Iy)
	print(val.Ixy)
	print()
	
	print('cent',Find_Centroid)(xy,val.Area)

	print('after -----------------------------------------------')

	val.profile_To_centriod()
	print(val.__doc__)
	print(val.cos_value)
	print(val.Ix)
	print(val.Iy)
	print(val.Ixy)
	print()
	print(  val.perimeter)
	s = val.stress_z(My = 110,Mx = -200,Nz =0)
	print( 'stress-->',s)



