#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
from graph import *
from graph_plugin import *
import graph_plugin
from profile_plugin import *
if __name__ == "__main__":	
	val = read_exe.Read_COS('../test_data/close_1.xlsx')
	
 	lis = val.cos_value	
 	lis.append([1.5,1])
 	lis.append([2.5,1])
 	print lis

 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)


	g.addEdge(1,8,1)
	g.addEdge(2,7,1)
	g.addEdge(3,6,1)

	g.remove_Edge(4,5)
	g.remove_Edge(6,7)
	g.remove_Edge(7,8)
	g.remove_Edge(10,9)
	g.remove_Edge(10,11)

	g.addEdge(10,8,1)
	g.addEdge(10,7,1)
	g.addEdge(11,7,1)
	g.addEdge(11,6,1)
	
	# draw_point_graph(g,dirddd,color='b')

	# for v in g:
	# 	print v
	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	new_dir = Pc.profile_To_centriod()

	print dirddd
	print new_dir
	graph_plugin.draw_point_graph(g,new_dir,color='b')


 