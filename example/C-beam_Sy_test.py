#coding:utf-8
#############################################################################
# debug in Sy
#############################################################################

import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
import profile
from graph import *
from graph_plugin import *
import open_profile
from open_profile import *
from profile_plugin import *

if __name__ == "__main__":	

 	# lis = [[-1,1],[0,1],[0,-1],[-1,-1]]

 	lis = [[-1,1],[-1,0],[1,0],[1,1]]

	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	val = Profile_Constant(graph = g,dir = dirddd)

	print val.__doc__
	print val.dir
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	
	val = Open_Profile(lis,val,Qx = 0,Qy = 1)
	# draw_point_graph(g, val.dir,color='b')

	draw_ShearFlow3D(g,dirddd,val.Shear_ST,[[0,1],[1,2],[2,3]],axis = 0)
	
	
