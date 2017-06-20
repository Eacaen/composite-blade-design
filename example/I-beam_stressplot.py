#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
import profile
from graph import *
from graph_plugin import *
from open_profile import *
from profile_plugin import *
if __name__ == "__main__":	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/gong2.xlsx')
	lis = val.cos_value	
	dirddd =cos_To_dict(lis)
	print dirddd
	
	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	
	g.addEdge(1,4,1)
	g.remove_Edge(2,3)

	# draw_point_graph(g,dirddd,color='b')

	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	Pc.profile_To_centriod()

	s = Pc.stress_z(My =-20,Mx = 20,Nz = 20)
	print s,type(s)
	draw_Stress(s,g,Pc.dir,linestyle= '--',axis = 0)

  
	