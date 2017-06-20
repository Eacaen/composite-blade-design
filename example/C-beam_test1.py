#coding:utf-8
#############################################################################
# move C-beam to its Centroid
# get its engineer constant value
# plot it out
#############################################################################

import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
import profile 
from graph_plugin import *

if __name__ == "__main__":	

	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[.xlsx')
	lis = val.cos_value	

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
	
	print Find_Centroid(val.dir,area  = val.Area),'cent'

	draw_point_graph(g, dirddd,color='b')
	print 'after -----------------------------------------------'

	print val.profile_To_centriod()
	print val.__doc__
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	print 'cent',Find_Centroid(val.dir,area  = val.Area)

	draw_point_graph(g, val.dir,color='b')