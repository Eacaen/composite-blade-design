#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *

if __name__ == "__main__":	
	# val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[]2.xlsx')	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/shape2.xlsx')	

	lis = val.cos_value	
	print lis
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,0.1)

	# draw_point_graph(g,dirddd,color='b')

	thk = graph_line_thickness(g,range(len(lis)))
	print '--------------------------',thk
	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	print 'area',Pc.Area
	print 'Ix-->',Pc.Ix
	print 'Iy-->',Pc.Iy
	print 'Ixy-->',Pc.Ixy
	new_dir = Pc.profile_To_centriod()
	print 'area',Pc.Area
	print 'Ix-->',Pc.Ix
	print 'Iy-->',Pc.Iy
	print 'Ixy-->',Pc.Ixy

	# draw_point_graph(g,Pc.dir ,color='b')
	cccc = dict_To_cos(Pc.dir)
	# cccc = [new_dir[0],new_dir[1]]

	val = open_profile.Open_Profile(cccc,Pc,thickness=thk,Qx = 0,Qy = 1)
	print '__doc__-->',val.__doc__
	print 'cos_value-->',val.cos_value
	print 'length-->',val.length
	print 'Ix-->',val.Ix
	print 'Iy-->',val.Iy
	print 'Ixy-->',val.Ixy
	print 'Sx-->',val.Sx
	print 'Sy-->-->',val.Sy
	print 'Shear_ST-->',val.Shear_ST
	
	A = open_profile.Surround_Area(val.cos_value,basic_point = [-1,0])

	Sxy = open_profile.get_Shear_center(cccc, Pc,thickness = thk ,basic_point = [0.5,0.5])
	print Sxy
 
	lin = line_value_package(range(len(lis)))
	draw_ShearFlow3D(g,dirddd,val.Shear_ST,lin,Shear_Center=Sxy,axis = 1)