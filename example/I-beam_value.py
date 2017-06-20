#coding:utf-8
#############################################################################
# move I-beam to its Centroid
# get its engineer constant value
# plot it out
#############################################################################

import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
from graph import *
import profile
import graph_plugin
from graph_plugin import *

if __name__ == "__main__":	

	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/gong_1_wai.xlsx')
	lis = val.cos_value	
	
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)


	g.addEdge(3,8,1)
	g.addEdge(0,9,1)
	g.remove_Edge(1,0)
	g.remove_Edge(5,6)
	val = Profile_Constant(graph = g,dir = dirddd)

	print val.__doc__
	print val.cos_value
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	
	print 'cent',Find_Centroid(graph = g,dir = dirddd,area  = val.Area)

	graph_plugin.draw_point_graph(g, val.dir,color='b')


	print 'after -----------------------------------------------'
	val.profile_To_centriod()
	print val.__doc__
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	print val.dir
	print 'cent',Find_Centroid(graph = g,dir = val.dir,area  = val.Area)
	# read_exe.draw_points(lis)
	graph_plugin.draw_point_graph(g, val.dir,color='b')