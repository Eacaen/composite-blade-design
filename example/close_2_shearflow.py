#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
import close_profile
from graph import *
from graph_plugin import *
import graph_plugin
from profile_plugin import *
if __name__ == "__main__":	
	val = read_exe.Read_COS('../test_data/close_2.xlsx')
	
 	lis = val.cos_value	
 	# lis.append([1,2])
 	# lis.append([3,2])
 	print lis

 	# lis[11] = [2.5,1]
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)
	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)

	dirddd[6] = [1,2]
	dirddd[7] = [3,2]

	g.addVertex(6)
	g.addVertex(7)

	g.addEdge(0,5,1)
	g.addEdge(1,4,1)


	g.remove_Edge(4,5)
	g.remove_Edge(4,3)
 
	g.addEdge(7,3,1)
	g.addEdge(7,4,1)
	g.addEdge(4,6,1)
	g.addEdge(6,5,1)

	for v in g:
		print v

	# draw_point_graph(g,dirddd,color='b')

	Pc = Profile_Constant(graph = g,dir = dirddd)
	
	new_dir = Pc.profile_To_centriod()

	# graph_plugin.draw_point_graph(g,new_dir,color='b')

#-------------------------------------------------------------------------#
	shear_flow = {}
	LL = []
	shear_flow_list = []

#-------------------------------------------------------------------------#
	ccc = [6,5,0,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

#-------------------------------------------------------------------------#
	ccc = [7,3,2,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

#-------------------------------------------------------------------------#
	ccc = [7,4]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
	len1 = val.length[0]
	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

#-------------------------------------------------------------------------#	

	ccc = [6,4]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
	len2 = val.length[0]
	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

#-------------------------------------------------------------------------#

	# ccc = [1,4]
	ccc = [4,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	Shear_ST = val.Shear_ST[0] + shear_flow_list[-2].subs(s,len1) + shear_flow_list[-1].subs(s,len2)
	shear_flow_list.append(Shear_ST)

#-------------------------------------------------------------------------#

	print LL
	# print shear_flow_list,range(0,len(shear_flow_list))
	aa = Shearflow_package(LL,shear_flow_list)
	print aa
	# print aa.values()

#-------------------------------------------------------------------------#
	liss1 = [6,5,0,1,4,6]
	liss2 = [7,4,1,2,3,7]
	
	thk_liss1 = graph_line_thickness(g,liss1)
	thk_liss2 = graph_line_thickness(g,liss2)

	Lis_g = [1000] * max(len(thk_liss1),len(thk_liss2))

	qp1 = close_profile.get_mutiCloseCells_Qp(new_dir,aa,liss1,thickness=thk_liss1,G = Lis_g )
	qp2 = close_profile.get_mutiCloseCells_Qp(new_dir,aa,liss2,thickness=thk_liss2,G = Lis_g )

	g1 = close_profile.get_mutiCloseCells_Gt(new_dir,liss1,thickness=thk_liss1,G = Lis_g )
	g2 = close_profile.get_mutiCloseCells_Gt(new_dir,liss2,thickness=thk_liss2,G = Lis_g )


	print '------------------',qp1,qp2,g1,g2
	A1 = Surround_Area(new_dir ,liss1,basic_point = [-1,0] )
	A2 = Surround_Area(new_dir ,liss2,basic_point = [1,0] )
	

	print '------------------'
	m1 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,liss1,basic_point = [-1,0] )

	m2 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,liss2,basic_point = [1,0] )

	pp = [0,0]
	m3 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,basic_point = pp )

	print 'mmmmm',m1,m2,m1+m2,m3
	aaaa =  close_profile.solve_Qn(area=[2*A1,2*A2],Gt =[[g1,2],[2,g2]],\
				Qp = [qp1,qp2,m3])

	print 'q1,q2,phi\n',aaaa
	ShearCenter = close_profile.get_mutiCloseCells_ShearCenter\
	(area=[2*A1,2*A2],Gt =[[g1,2],[2,g2]],Qp = [qp1,qp2,m3],Q=1)

	print ShearCenter[2]+pp[0],'\n'


	print close_profile.get_resultant_Q(new_dir,aa)

	bb = close_profile.update_mutiCloseCells_Shearflow(aa,[6,5,0,1],aaaa[0])
	bb = close_profile.update_mutiCloseCells_Shearflow(bb,[6,4,1],-aaaa[0])
	m1 = close_profile.get_mutiCloseCells_Moment(new_dir,bb,liss1,basic_point = [-1,0] )
	print m1

	cc = close_profile.update_mutiCloseCells_Shearflow(aa,[7,3,2,1],-aaaa[1])
	cc = close_profile.update_mutiCloseCells_Shearflow(cc,[7,4,1],aaaa[1])
	m2 = close_profile.get_mutiCloseCells_Moment(new_dir,cc,liss2,basic_point = [1,0] )
	print m2
 
	ee = close_profile.update_mutiCloseCells_Shearflow(aa,[6,5,0,1],aaaa[0])
	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[6,4,1],-aaaa[0])

	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[7,3,2,1],-aaaa[1])
	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[7,4,1],aaaa[1])
	m3 = close_profile.get_mutiCloseCells_Moment(new_dir,ee,basic_point = [0,0] )
	print m3
 
	print close_profile.get_resultant_Q(new_dir,ee)

	# draw_ShearFlow3D(g,new_dir,Shear_Flow= ee.values(),num_list = LL,Shear_Center =[0,0],\
	# 							axis = 0,gif=0)