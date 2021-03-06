#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
import close_profile
from graph import *
from graph_plugin import *
from profile_plugin import *

if __name__ == "__main__":	

	val = read_exe.Read_COS('../test_data/naca2412.xlsx')	

	lis = val.cos_value	
	# print(lis)
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,0.1)

	# draw_point_graph(g,dirddd,color='b',axis = 'equal')

	thk = graph_line_thickness(g,range(len(lis)))
	# print('--------------------------',thk)
	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	

	# print('area',Pc.Area)
	# print('Ix-->',Pc.Ix)
	# print('Iy-->',Pc.Iy)
	# print('Ixy-->',Pc.Ixy)
	new_dir = Pc.profile_To_centriod()

	# draw_point_graph(g,new_dir,color='b',axis = 'equal')

	# print('area',Pc.Area)
	# print('Ix-->',Pc.Ix)
	# print('Iy-->',Pc.Iy)
	# print('Ixy-->',Pc.Ixy)

	# draw_point_graph(g,Pc.dir ,color='b')
	cccc = dict_To_cos(Pc.dir)
	# cccc = [new_dir[0],new_dir[1]]

	val = open_profile.Open_Profile(cccc,Pc,thickness=thk,Qx = 1,Qy = 0)
	# print('__doc__-->',val.__doc__)
	# print('cos_value-->',val.cos_value)
	# print('length-->',val.length)
	# print('Ix-->',val.Ix)
	# print('Iy-->',val.Iy)
	# print('Ixy-->',val.Ixy)
	# print('Sx-->',val.Sx)
	# print('Sy-->-->',val.Sy)
	# print('Shear_ST-->',val.Shear_ST)
	
	A = open_profile.Surround_Area(val.cos_value,basic_point = [0,0])

	Sxy = close_profile.close_Shear_center(cccc, Pc,thickness = thk ,basic_point = [0.5,0.5])
	print(Sxy,A)
	# draw_point_graph(g,new_dir,color='b',axis = 'equal',Show_Number = 0,Shear_Center=Sxy)

	Qo = open_profile.get_Shear_Qo(val.Shear_ST, val.cos_value)

	# print(cccc == val.cos_value)
	Shear_ST = [n + Qo / (2*A) for n in val.Shear_ST]
	lin = line_value_package(range(len(lis)))
	draw_ShearFlow3D(g,new_dir,Shear_ST,lin,Shear_Center=Sxy,axis = 1,gif = 0\
			,pbaspect = [1,10,1],Show_Number=0,Load=[1,-1])