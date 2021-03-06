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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/rhombus.xlsx')
	
	lis = val.cos_value	

	# read_exe.draw_points(val.cos_value)

	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	
	g.addEdge(0,3,1)

	draw_point_graph(g,dirddd,color='b')
	
	val = Profile_Constant(graph = g,dir = dirddd)

	print val.__doc__
	print val.dir
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	
	print 'cent',Find_Centroid(val.dir,area  = val.Area)

	print 'after -----------------------------------------------'

	val.profile_To_centriod()
	print val.__doc__
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	ddd = val.dir
	print 'cent',Find_Centroid(val.dir,area  = val.Area)

	draw_point_graph(g,ddd,color='b')