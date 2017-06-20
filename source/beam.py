import numpy as np
import scipy as sp
import sympy as syp
import math
import copy

class Cantilever_Beam(object):
	"""docstring for Cantilever_Beam"""
	def __init__(self,profile_constant=None,Length=1,perimeter=0,Ix=0,Iy=0,Material = None,Ex=0,Ey=0,load=[],Fx=None,Fy=None,Mz = None):
		super(Cantilever_Beam, self).__init__()

		if profile_constant:
			self.Ix = profile_constant.Ix
			self.Iy = profile_constant.Iy
			self.Ixy = profile_constant.Ixy
			self.perimeter = profile_constant.perimeter
		else:
			self.Ix = Ix
			self.Iy = Iy
			self.perimeter = perimeter

		self.load = load

		self.Fx = Fx
		self.Fy = Fy
		self.Mz = Mz
		
		self.Ex = Ex
		self.Ey = Ey

		self.Length = Length

		self.deflection_x = 0
		self.deflection_y = 0
		self.angle_x = 0
		self.angle_y = 0

		if Material:
			self.mass = Material.density * profile_constant.Area *self.Length 
			self.Ex = Material.Ex
			self.Ey = Material.Ey
 
		self.update()
#-----------------------------------------------------------
#			P*L^2
# \theta = -------
#			 2 EI
#      P*L^3
# w = -------
# 	    3 EI
#-----------------------------------------------------------
	def update(self):
		if self.Fx:
			self.deflection_x = self.Fx * self.Length**3 / (3*self.Ex*self.Ix)
			self.angle_x = self.Fx * self.Length**2 / (2*self.Ex*self.Ix)
		if self.Fy:
			self.deflection_y = self.Fy * self.Length**3 / (3*self.Ey*self.Iy)
			self.angle_y = self.Fy * self.Length**2 / (2*self.Ey*self.Iy)

	def change_load(load=[],Fx=None,Fy=None):
		self.load = load
		self.Fx = Fx
		self.FY = Fy
		self.Mz = Mz
		self.update()

	def change_parameter(Length,Ex=0,Ey=0):
		self.Length = Length
		self.Ex = Ex
		self.Ey = Ey
		self.update()

if __name__ == "__main__":
	from profile import *
 	xy = [[-2,-1],[0,-1],[0,1],[-2,1]]
	tk = 1*np.ones(len(xy)-1)
	val = Profile_Constant(xy,tk)

	b = Cantilever_Beam(val, 10,Ex = 500,Fx = 10)
	print b.deflection_x
