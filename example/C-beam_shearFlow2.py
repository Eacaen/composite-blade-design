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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/]--|_|.xlsx')
	lis = val.cos_value	
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)
 

	# draw_point_graph(g,dirddd,color='b')

	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	lis = Pc.profile_To_centriod()
	ccc = [0,1,2,3]
	cccc = [lis[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	print 'ccccc--',cccc

	val = open_profile.Open_Profile(cccc,Pc,thickness=thk , Qx = 0,Qy =1)

	leng = graph_line_length(g,dirddd,ccc)
	# draw_ShearFlow(val.Shear_ST,val.length)
 
	print 'Iy-->',val.Iy
	print 'Ixy-->',val.Ixy
	print 'Sx-->',val.Sx
	print 'Sy-->',val.Sy
	print 'Shear_ST-->',val.get_Shear_ST()
 
	draw_ShearFlow3D_gif(g,dirddd,val.Shear_ST,[[0,1],[1,2],[2,3]],axis = 1,save =0,name = '')

	