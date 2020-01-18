#coding:utf-8
#############################################################################
#  
#  
#  
#############################################################################

import numpy as np
import scipy as sp
import sympy as syp
from sympy import *
import math
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.mplot3d 
import matplotlib.animation as animation
from profile import *
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from profile_toolbox import *

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


def draw_ShearFlow(Shear_Flow ,length ,linewidth = 1 ,linestyle= '-',Shear_Center = []):
	if Shear_Flow:
		for n in range(0,len(Shear_Flow)):
			xl = np.linspace(0,length[n],100)
			yl = []
			for i in xl:
				yl.append(Shear_Flow[n].subs(s,i))
			
			plt.plot(xl,yl,linewidth = linewidth,linestyle = linestyle)
			plt.text(xl[99],yl[99], n,color='red',fontsize=18) 
			plt.plot([0,xl[99]],[yl[99],yl[99]],color = 'black',linestyle = '-.')

		if Shear_Center != []:
			xs = Shear_Center[0]
			ys = Shear_Center[1]
			plt.plot(xs,ys,maker = 'o',color = 'r')

		plt.grid()
		plt.show()

def draw_ShearFlow3D(graph,dir=[],Shear_Flow=[],num_list=[],ShearFlow_package=[],Shear_Center = [],\
	linewidth = 1 ,linestyle= '-',axis = True , pbaspect = [],Show_Number = True,Number_Size = 10,Number_Average=5,\
		gif = False,save = False , name = '',title = '',Load = []):

	xdir = [float(dir[i][0]) for i in range(0,len(dir))]
	ydir = [float(dir[i][1]) for i in range(0,len(dir))]
	addTiT = ''
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-', color='r', shrinkA=0, shrinkB=0)

	max_x = int(max([(num) for num in xdir])) +1
	min_x = int(min([(num) for num in xdir])) -1

	max_y = int(max([(num) for num in ydir])) +1
	min_y = int(min([(num) for num in ydir])) -1
	ax.set_ylim(min_x,max_x)
	ax.set_zlim(min_y,max_y)

################################### Draw profile #########################################
	for v in graph:
		for e in v.getConnections():
			xx = np.linspace(xdir[v.id],xdir[e.id],5)
			yy = np.linspace(ydir[v.id],ydir[e.id],5)
			zeo = np.zeros(len(xx))
			ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')


################################# Draw shear flow #######################################

	for i in range(0,len(num_list)):

		p1 = num_list[i][0]
		p2 = num_list[i][1]
		p11 = dir[p1]
		p22 = dir[p2]
		leng = math.sqrt((p11[0] - p22[0])**2 + (p11[1] - p22[1])**2)

		le = np.linspace(0,leng,100)
		zz = []
		for n in le:
			zz.append(Shear_Flow[i].subs(s,n))
		
		xx = np.linspace(round(p11[0],2) , round(p22[0],2),100)
		yy = np.linspace(round(p11[1],2) , round(p22[1],2),100)

		plt.plot(zz,xx,yy,linewidth = linewidth,linestyle = linestyle)

################################### draw arrow ########################################
	for i in range(len(num_list)):

		p1 = num_list[i][0] ; p2 = num_list[i][1]
		p11 = dir[p1]  ; p22 = dir[p2]
		leng = math.sqrt((p11[0] - p22[0])**2 + (p11[1] - p22[1])**2)

		le = np.linspace(0,leng,Number_Average)
		zz = []
		xx = np.linspace(round(p11[0],2) , round(p22[0],2),Number_Average)
		yy = np.linspace(round(p11[1],2) , round(p22[1],2),Number_Average)

		for n in le:
			sF = float(Shear_Flow[i].subs(s,n))
			zz.append(sF)
		
		for n in range(len(xx)):
			a = Arrow3D([0,zz[n]],[xx[n],xx[n]],[yy[n],yy[n]], **arrow_prop_dict)
			ax.add_artist(a)
################################### put the num_listber ########################################
	if Show_Number:
		for i in range(len(dir)):
			ax.text(0,xdir[i],ydir[i] , i, family='serif',style='italic', ha='right', wrap=True,\
										color='blue',fontsize=Number_Size)


################################### draw Shear_Center ########################################
	if Shear_Center != []:
		xs = round(Shear_Center[0],2)
		ys = round(Shear_Center[1],2)
		ax.plot([0],[xs],[ys],'ro')

		ax.text(0,xs,ys ,'Shear Center', family='serif',style='italic', ha='right', wrap=True,\
										color='blue',fontsize=10)
################################### draw Load at Shear_Center  ########################################
		if Load != []:
			addTiT = ''
			LOad_arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', \
					color='r', shrinkA=0, shrinkB=0)

			Mx = max_x / 5.0
			My = max_y / 5.0
			try:
				Qx = Load[0]

				if Qx > 0:
					a = Arrow3D([0,0],[xs,xs+Qx + Mx],[ys,ys], **LOad_arrow_prop_dict)
					ax.add_artist(a)
				if Qx < 0:
					a = Arrow3D([0,0],[xs,xs+Qx - Mx],[ys,ys], **LOad_arrow_prop_dict)	
					ax.add_artist(a)
				addTiT = addTiT + ' Qx = ' + str(Qx)
			except:
				Qx = 0
			try:
				Qy = Load[1]
				if Qy > 0:
					a = Arrow3D([0,0],[xs,xs],[ys,ys+Qy+ My], **LOad_arrow_prop_dict)
					ax.add_artist(a)
				if Qy < 0:
					a = Arrow3D([0,0],[xs,xs],[ys,ys+Qy- My], **LOad_arrow_prop_dict)
					ax.add_artist(a)
				addTiT = addTiT + ' Qy = ' + str(Qy)
			except:
				Qy = 0

			try:
				Mz = abs(Load[2])

			 	# ax.annotate("",xy=(0,xs, ys-Mz), xycoords='data',
			 	# xytext=(0,xs,ys+Mz), textcoords='data',
     #            arrowprops=dict(arrowstyle="->", #linestyle="dashed",
     #                            color="red",
     #                            shrinkA=5, shrinkB=5,
     #                            patchA=None,
     #                            patchB=None,
     #                            connectionstyle="angle3,angleA=90,angleB=0",
     #                            ),
     #            )
				addTiT = addTiT + ' Mz = ' + str(Mz)
			except:
				Mz = 0 
		


	ax.set_xlabel('Z')
	ax.set_ylabel('X')
	ax.set_zlabel('Y')
	
	if not axis:
		ax.set_axis_off()

	TiT = 'Shear Flow in the profile\n'+addTiT+title
	plt.title(TiT, loc = 'left')

	if gif:
		def simData():  
			T1 = list(range(0,361))
			T2 = range(0,360)
			T2.reverse()
			T1[len(T1):len(T1)] = T2
			while 1:
				for i in range(len(T1)):
					t = T1[i]
					yield t 
		        
		def zhuan(simData):
			angle = simData
			ax.view_init(30, angle)
			return ax
			
		animator = animation.FuncAnimation(fig, zhuan,simData,\
				blit=False, interval=10,repeat=True)

		if save and name:
			Name = str(name) + '.mp4'
			animator.save(Name, fps=30,
		                 extra_args=['-vcodec', 'libx264'],
		                 writer='ffmpeg_file')
	# plt.axis('equal')#useless
	# ax.set_aspect('equal') #useless
	if pbaspect:
		ax.pbaspect = pbaspect #useless
	# ax.auto_scale_xyz([-10,10],[min_x,max_x],[min_y, max_y])
	plt.draw()
	plt.show()

 

############################################################################################

def draw_Stress(stress,graph,dir=[],num_list=[],linewidth = 1 ,linestyle= '-',arrowstyle='-|>'\
			,Show_Number = True,Number_Size = 10,Number_Average = 5\
			,axis = True,gif = False,save = False , name = '',Load=[],unit = 1):
	a = syp.Wild('a')
	b = syp.Wild('b')
	c = syp.Wild('c')
	x = syp.symbols('x')
	y = syp.symbols('y')
	
	ccc = syp.collect(stress,[x,y],evaluate=False)
	try:
		a1 = float(ccc[x])
	except:
		a1 = 0

	try:
		b1 = float(ccc[y])
	except:
		b1 = 0

	try:
		c1 = float(ccc[S(1)])
	except:
		c1 = 0

	xdir = [float(dir[i][0])/unit for i in range(0,len(dir))]
	ydir = [float(dir[i][1])/unit for i in range(0,len(dir))]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	arrow_prop_dict = dict(mutation_scale=20, arrowstyle=arrowstyle, color='r', shrinkA=0, shrinkB=0)

################################### Draw profile #########################################
	for v in graph:
		for e in v.getConnections():
			xx = np.linspace(xdir[v.id],xdir[e.id],5)
			yy = np.linspace(ydir[v.id],ydir[e.id],5)
			zeo = np.zeros(len(xx))
			ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')


#######################################################################################
	if num_list == []:
		for v in graph:
			for e in v.getConnections():
				thick_ij = v.getWeight(e)
				if thick_ij != 0:
					xx = np.linspace(xdir[v.id],xdir[e.id],5)
					yy = np.linspace(ydir[v.id],ydir[e.id],5)
					zz = a1*xx + b1*yy + c1

					ax.plot(zz, xx,yy , linewidth = linewidth ,linestyle = linestyle)

					zeo = np.zeros(len(xx))
					ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')

		for v in graph:
			for e in v.getConnections():
				thick_ij = v.getWeight(e)
				if thick_ij != 0:
					xx = np.linspace(xdir[v.id],xdir[e.id],Number_Average)
					yy = np.linspace(ydir[v.id],ydir[e.id],Number_Average)
					kk = []
					for i in range(len(xx)):
						high = a1 * xx[i] + b1 * yy[i] + c1
						
						if high > 0:
							a = Arrow3D([0,high],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
						elif high < 0:
							a = Arrow3D([high,0],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
						ax.add_artist(a)

	if num_list:
		for i in range(len(num_list)):
			m = num_list[i][0]
			n = num_list[i][1]

			xx = np.linspace(xdir[m],xdir[n],5)
			yy = np.linspace(ydir[m],ydir[n],5)
			zz = a1*xx + b1*yy + c1
			ax.plot(zz, xx,yy , linewidth = linewidth ,linestyle = linestyle)

			zeo = np.zeros(len(xx))
			ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')

		for i in range(len(num_list)): 
			m = num_list[i][0]
			n = num_list[i][1]
			xx = np.linspace(xdir[m],xdir[n],Number_Average)
			yy = np.linspace(ydir[m],ydir[n],Number_Average)
			kk = []
			for i in range(len(xx)):
				high = a1 * xx[i] + b1 * yy[i] + c1
					
				if high > 0:
					a = Arrow3D([0,high],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
				elif high < 0:
					a = Arrow3D([high,0],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
				ax.add_artist(a)


	if Show_Number:
		if num_list == []:
			for i in range(len(dir)):
				ax.text(0,xdir[i],ydir[i] , i, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)
		if num_list:
			for i in range(len(num_list)): 
				m = num_list[i][0]
				n = num_list[i][1]
				ax.text(0,xdir[m],ydir[m] , m, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)

				ax.text(0,xdir[n],ydir[n] , n, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)
	ax.set_xlabel('Z')
	ax.set_ylabel('X')
	ax.set_zlabel('Y')

	addTiT = ''
	if Load:
		try:
			Mx = Load[0]
			addTiT = addTiT + ' Mx = ' + str(Mx)
		except:
			Mx = 0

		try:
			My = Load[1]
			addTiT = addTiT + ' My = ' + str(My)
		except:
			My = 0

		try:
			Nz = Load[2]
			addTiT = addTiT + ' Nz = ' + str(Nz)
		except:
			Nz = 0

	TiT = ' in the profile\n'+addTiT
	plt.title(r'$\sigma_z$'+TiT, loc = 'left')

	if not axis:
		ax.set_axis_off()

	if gif:
		def simData():  
			T1 = list(range(0,361))
			T2 = range(0,360)
			T2.reverse()

			T1[len(T1):len(T1)] = T2
			while 1:
				for i in range(len(T1)):
					t = T1[i]
					yield t 
		        
		def zhuan(simData):
			angle = simData
			ax.view_init(30, angle)
			return ax
			
		animator = animation.FuncAnimation(fig, zhuan,simData,\
				blit=False, interval=10,repeat=True)

		if save and name:
			Name = str(name) + '.mp4'
			animator.save(Name, fps=30,
		                 extra_args=['-vcodec', 'libx264'],
		                 writer='ffmpeg_file')

	plt.draw()
	plt.show()


############################################################################################

def draw_Stress_2(stress_package,graph,dir=[],num_list=[],linewidth = 1 ,linestyle= '-',arrowstyle='-|>'\
			,Show_Number = True,Number_Size = 10,Number_Average = 5\
			,axis = True,gif = False,save = False , name = '',Load=[],unit = 1):
	a = syp.Wild('a')
	b = syp.Wild('b')
	c = syp.Wild('c')
	x = syp.symbols('x')
	y = syp.symbols('y')
	


	xdir = [float(dir[i][0])/unit for i in range(0,len(dir))]
	ydir = [float(dir[i][1])/unit for i in range(0,len(dir))]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	arrow_prop_dict = dict(mutation_scale=20, arrowstyle=arrowstyle, color='r', shrinkA=0, shrinkB=0)

################################### Draw profile #########################################
	for v in graph:
		for e in v.getConnections():
			xx = np.linspace(xdir[v.id],xdir[e.id],5)
			yy = np.linspace(ydir[v.id],ydir[e.id],5)
			zeo = np.zeros(len(xx))
			ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')


#######################################################################################
	if num_list == []:
		for v in graph:
			for e in v.getConnections():

				thick_ij = v.getWeight(e)
				if thick_ij != 0:

					try:
						ccc = syp.collect(stress_package[(v.id,e.id)],[x,y],evaluate=False)
					except:
						ccc = syp.collect(stress_package[(e.id,v.id)],[x,y],evaluate=False)
				
					try:
						a1 = float(ccc[x])
					except:
						a1 = 0

					try:
						b1 = float(ccc[y])
					except:
						b1 = 0

					try:
						c1 = float(ccc[S(1)])
					except:
						c1 = 0

					xx = np.linspace(xdir[v.id],xdir[e.id],Number_Average)
					yy = np.linspace(ydir[v.id],ydir[e.id],Number_Average5)
					zz = a1*xx + b1*yy + c1

					ax.plot(zz, xx,yy , linewidth = linewidth ,linestyle = linestyle)

					zeo = np.zeros(len(xx))
					ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')

		for v in graph:
			for e in v.getConnections():
				thick_ij = v.getWeight(e)
				if thick_ij != 0:

					try:
						ccc = syp.collect(stress_package[(v.id,e.id)],[x,y],evaluate=False)
					except:
						ccc = syp.collect(stress_package[(e.id,v.id)],[x,y],evaluate=False)
				
					try:
						a1 = float(ccc[x])
					except:
						a1 = 0

					try:
						b1 = float(ccc[y])
					except:
						b1 = 0

					try:
						c1 = float(ccc[S(1)])
					except:
						c1 = 0

					xx = np.linspace(xdir[v.id],xdir[e.id],Number_Average)
					yy = np.linspace(ydir[v.id],ydir[e.id],Number_Average)
					kk = []
					for i in range(len(xx)):
						high = a1 * xx[i] + b1 * yy[i] + c1
						
						if high > 0:
							a = Arrow3D([0,high],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
						elif high < 0:
							a = Arrow3D([high,0],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
						ax.add_artist(a)

	if num_list:
		for i in range(len(num_list)):
			m = num_list[i][0]
			n = num_list[i][1]

			ccc = syp.collect(stress_package[(m,n)],[x,y],evaluate=False)
				
			try:
				a1 = float(ccc[x])
			except:
				a1 = 0
			try:
				b1 = float(ccc[y])
			except:
				b1 = 0
			try:
				c1 = float(ccc[S(1)])
			except:
				c1 = 0

			xx = np.linspace(xdir[m],xdir[n],Number_Average)
			yy = np.linspace(ydir[m],ydir[n],Number_Average)
			zz = a1*xx + b1*yy + c1
			ax.plot(zz, xx,yy , linewidth = linewidth ,linestyle = linestyle)

			zeo = np.zeros(len(xx))
			ax.plot(zeo,xx,yy,linewidth = 3 ,color = 'black')

		for i in range(len(num_list)): 
			m = num_list[i][0]
			n = num_list[i][1]
			xx = np.linspace(xdir[m],xdir[n],Number_Average)
			yy = np.linspace(ydir[m],ydir[n],Number_Average)
			kk = []

			ccc = syp.collect(stress_package[(m,n)],[x,y],evaluate=False)
				
			try:
				a1 = float(ccc[x])
			except:
				a1 = 0
			try:
				b1 = float(ccc[y])
			except:
				b1 = 0
			try:
				c1 = float(ccc[S(1)])
			except:
				c1 = 0

			for i in range(len(xx)):
				high = a1 * xx[i] + b1 * yy[i] + c1
					
				if high > 0:
					a = Arrow3D([0,high],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
				elif high < 0:
					a = Arrow3D([high,0],[xx[i],xx[i]],[yy[i],yy[i]], **arrow_prop_dict)
				ax.add_artist(a)


	if Show_Number:
		if num_list == []:
			for i in range(len(dir)):
				ax.text(0,xdir[i],ydir[i] , i, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)
		if num_list:
			for i in range(len(num_list)): 
				m = num_list[i][0]
				n = num_list[i][1]
				ax.text(0,xdir[m],ydir[m] , m, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)

				ax.text(0,xdir[n],ydir[n] , n, family='serif',style='italic', ha='right', wrap=True,\
												color='blue',fontsize=Number_Size)
	ax.set_xlabel('Z')
	ax.set_ylabel('X')
	ax.set_zlabel('Y')

	addTiT = ''
	if Load:
		try:
			Mx = Load[0]
			addTiT = addTiT + ' Mx = ' + str(Mx)
		except:
			Mx = 0

		try:
			My = Load[1]
			addTiT = addTiT + ' My = ' + str(My)
		except:
			My = 0

		try:
			Nz = Load[2]
			addTiT = addTiT + ' Nz = ' + str(Nz)
		except:
			Nz = 0

	TiT = ' in the profile\n'+addTiT
	plt.title(r'$\sigma_z$'+TiT, loc = 'left')

	if not axis:
		ax.set_axis_off()

	if gif:
		def simData():  
			T1 = list(range(0,361))
			T2 = range(0,360)
			T2.reverse()
			T1[len(T1):len(T1)] = T2
			while 1:
				for i in range(len(T1)):
					t = T1[i]
					yield t 
		        
		def zhuan(simData):
			angle = simData
			ax.view_init(30, angle)
			return ax
			
		animator = animation.FuncAnimation(fig, zhuan,simData,\
				blit=False, interval=10,repeat=True)

		if save and name:
			Name = str(name) + '.mp4'
			animator.save(Name, fps=30,
		                 extra_args=['-vcodec', 'libx264'],
		                 writer='ffmpeg_file')

	plt.draw()
	plt.show()


def Shearflow_package(ccos_value,shear_flow):
	from collections import OrderedDict
	sf_pack = OrderedDict()
	for i in range(len(shear_flow)):
			ccos = ( ccos_value[i][0],ccos_value[i][1]) 
			sf_pack[ccos] = shear_flow[i]
	return sf_pack


############################################################
#  		  /l       /l 
#    Sa  =| p*ds = |  dot_To_line * ds 
#         /0       /0
############################################################
def Surround_Area(dir,num_list=[],basic_point = [0,0] ):
	Sa = 0

	cos_value = [dir[n] for n in num_list]

	if not is_point_in(basic_point, cos_value):
		raise 'basic point not in profile,Choose another one'

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

############################################################################################
def Length(dir,num_list):
	point1 = dir[num_list[0]]
	point2 = dir[num_list[1]]

	xs = point1[0] ; ys = point1[1]
	xe = point2[0] ; ye = point2[1]
	yy = ye - ys
	xx = xe - xs
	length = math.sqrt(yy**2+xx**2)
	return length

############################################################################################
def Max_ShearFlow(graph,dir=[],Shear_Flow=[],num_list=[]):

	xdir = [float(dir[i][0]) for i in range(0,len(dir))]
	ydir = [float(dir[i][1]) for i in range(0,len(dir))]
 
	max_SF = 0
	min_SF = 0
	for i in range(0,len(num_list)):

		p1 = num_list[i][0] ; p2 = num_list[i][1]
		p11 = dir[p1]  ; p22 = dir[p2]
		leng = math.sqrt((p11[0] - p22[0])**2 + (p11[1] - p22[1])**2)

		le = np.linspace(0,leng,20)
		zz = []
		for n in le:
			zz.append(Shear_Flow[i].subs(s,n))

			a = max(zz)
			if a > max_SF:
				max_SF = a
			b = min(zz)
			if b < min_SF:
				min_SF = b

	return [max_SF,min_SF]
	 
		 
##############################################################################

def Max_Stress(stress,graph,dir=[],num_list=[],Number_Average=5):
	a = syp.Wild('a')
	b = syp.Wild('b')
	c = syp.Wild('c')
	x = syp.symbols('x')
	y = syp.symbols('y')
	
	ccc = syp.collect(stress,[x,y],evaluate=False)
	try:
		a1 = float(ccc[x])
	except:
		a1 = 0

	try:
		b1 = float(ccc[y])
	except:
		b1 = 0

	try:
		c1 = float(ccc[S(1)])
	except:
		c1 = 0

	xdir = [float(dir[i][0]) for i in range(0,len(dir))]
	ydir = [float(dir[i][1]) for i in range(0,len(dir))]

	max_stress = 0
	min_stress = 0
	if num_list == []:
		for v in graph:
			for e in v.getConnections():
				thick_ij = v.getWeight(e)
				if thick_ij != 0:
					xx = np.linspace(xdir[v.id],xdir[e.id],Number)
					yy = np.linspace(ydir[v.id],ydir[e.id],Number)
					zz = a1*xx + b1*yy + c1

					a = max(zz)
					if a > max_stress:
						max_stress = a
					b = min(zz)
					if b < min_stress:
						min_stress = b
	if num_list:
		for i in range(len(num_list)):
			m = num_list[i][0]
			n = num_list[i][1]

			xx = np.linspace(xdir[m],xdir[n],Number_Average)
			yy = np.linspace(ydir[m],ydir[n],Number_Average)
			zz = a1*xx + b1*yy + c1

			a = max(zz)
			if a > max_stress:
				max_stress = a
			b = min(zz)
			if b < min_stress:
				min_stress = b

	return [max_stress,min_stress]
#------------------------------------------------------------------------------------------#

if __name__ == "__main__":
	Shear_ST = [-0.1*s**2, -0.1*s - 0.1, 0.05*s**2 - 0.1*s - 0.5, 0.1*s - 0.5, -0.1*s**2 + 0.2*s - 0.1]
	le = [1,4,2,4,1]
	# stress = 37.5*x + 21.4285714285714*y + 16.6666666666667
	

	# draw_ShearFlow(Shear_ST,le)

#########################################################################################
	import read_exe
	from graph_plugin import *

	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[.xlsx')
	lis = val.cos_value	

	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	stress = -75.0*x + 23.5714285714286*y + 50
	draw_Stress(stress,g,dirddd,linestyle= '--',arrowstyle='-|>')
	# draw_ShearFlow3D(g,dirddd,Shear_ST,[[0,1],[1,2],[2,3]],\
	# 		Shear_Center = [0.5,3],Load=[1,-1])
