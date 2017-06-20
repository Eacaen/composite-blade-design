#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
from profile_plugin import *

import mpl_toolkits.mplot3d 
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
if __name__ == "__main__":	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/|_|1.xlsx')
	lis = val.cos_value	
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)
 

	# draw_point_graph(g,dirddd,color='b')

	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	new_dir = Pc.profile_To_centriod()

	print 'Ix-->',Pc.Ix
	print 'Iy-->',Pc.Iy
	print 'Ixy-->',Pc.Ixy


	ccc = [0,1,2,3]
	cccc = [new_dir[i] for i in ccc]
	thk = graph_line_thickness(g,ccc)

	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	leng = graph_line_length(g,dirddd,ccc)
	# draw_ShearFlow(val.Shear_ST,val.length)
	


	# print '__doc__-->',val.__doc__
	# print 'cos_value-->',val.cos_value
	# print 'length-->',val.length
	print 'Ix-->',val.Ix
	print 'Iy-->',val.Iy
	print 'Ixy-->',val.Ixy
	print 'Sx-->',val.Sx
	print 'Sy-->',val.Sy
	print 'Shear_ST-->',val.get_Shear_ST()
	
	# tk = graph_line_thickness(g,[0,1,4,3])
	# print 'tk',tk
	Sxy = open_profile.get_Shear_center(cccc, Pc,thickness = thk ,basic_point = [0.5,0.5])
	print Sxy
	# draw_ShearFlow3D(g,dirddd,val.Shear_ST,[[0,1],[1,2],[2,3]],Shear_Center=Sxy,axis = 1)

	