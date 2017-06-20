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
	val = read_exe.Read_COS('../test_data/gong2.xlsx')
	
 	lis = val.cos_value
 	# lis[5] = [6,3]
 	# lis.reverse()
 	print lis
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	
	g.addEdge(1,4,2)
	g.remove_Edge(2,3)

	# draw_point_graph(g,dirddd,color='b')

	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	new_dir = Pc.profile_To_centriod()

#-------------------------------------------------------------------------#
	shear_flow = {}
	LL = []
	shear_flow_list = []

#-------------------------------------------------------------------------#
	ccc = [3,4]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =0,Qy = 1)
	len1 = val.length[0]
	LL.append(ccc)
	shear_flow_list.append(val.Shear_ST[0])

#-------------------------------------------------------------------------#
	ccc = [5,4]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =0,Qy = 1)
	len2 = val.length[0]

	LL.append(ccc)
	shear_flow_list.append(val.Shear_ST[0])

#-------------------------------------------------------------------------#
	ccc = [4,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =0,Qy = 1)
	LL.append(ccc)
	Shear_ST = val.Shear_ST[0] + shear_flow_list[0].subs(s,len1) + shear_flow_list[1].subs(s,len2)
	shear_flow_list.append(Shear_ST)

#-------------------------------------------------------------------------#

	ccc = [0,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =0,Qy = 1)
	LL.append(ccc)
	shear_flow_list.append(val.Shear_ST[0])

#-------------------------------------------------------------------------#

	ccc = [2,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =0,Qy = 1)
	LL.append(ccc)
	shear_flow_list.append(val.Shear_ST[0])

#-------------------------------------------------------------------------#

	print LL,range(0,len(LL))
	print shear_flow_list,range(0,len(shear_flow_list))
 	draw_ShearFlow3D(g,dirddd,Shear_Flow= shear_flow_list,num_list = LL,axis = 1,gif=0)
