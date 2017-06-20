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

	# graph_plugin.draw_point_graph(g,new_dir,color='b')

#-------------------------------------------------------------------------#
	shear_flow = {}
	LL = []
	shear_flow_list = []

#-------------------------------------------------------------------------#
	ccc = [9,8]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)
#-------------------------------------------------------------------------#
	ccc = [10,8]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)
	
	aa = Shearflow_package(LL,shear_flow_list)
#-------------------------------------------------------------------------#
	ccc = [8,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))

	SSS = val.Shear_ST[0] + aa[(9,8)].subs(s,Length(new_dir,[9,8])) + aa[(10,8)].subs(s,Length(new_dir,[10,8]))

	shear_flow_list.append(SSS)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	
	ccc = [0,1]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))
 
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	
	ccc = [1,2]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))

	SSS = val.Shear_ST[0] + aa[(0,1)].subs(s,Length(new_dir,[0,1])) + \
					aa[(8,1)].subs(s,Length(new_dir,[8,1]))

	shear_flow_list.append(SSS)

	aa = Shearflow_package(LL,shear_flow_list)

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

	ccc = [5,6]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)
#-------------------------------------------------------------------------#
	ccc = [11,6]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)

	LL.extend(line_value_package(ccc))
	shear_flow_list.extend(val.Shear_ST)
	
	aa = Shearflow_package(LL,shear_flow_list)
#-------------------------------------------------------------------------#
	ccc = [6,3]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))

	SSS = val.Shear_ST[0] + aa[(5,6)].subs(s,Length(new_dir,[5,6])) + \
							aa[(11,6)].subs(s,Length(new_dir,[11,6]))

	shear_flow_list.append(SSS)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	
	ccc = [4,3]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))
 
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	
	ccc = [3,2]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))

	SSS = val.Shear_ST[0] + aa[(6,3)].subs(s,Length(new_dir,[6,3])) + \
					aa[(4,3)].subs(s,Length(new_dir,[4,3]))

	shear_flow_list.append(SSS)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	

	ccc = [10,7]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))
 
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)
	

#-------------------------------------------------------------------------#	

	ccc = [11,7]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))
 
	shear_flow_list.extend(val.Shear_ST)

	aa = Shearflow_package(LL,shear_flow_list)

#-------------------------------------------------------------------------#	
	ccc = [7,2]
 	cccc = [new_dir[i] for i in ccc]

	thk = graph_line_thickness(g,ccc)
	val = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
 
 	LL.extend(line_value_package(ccc))

	SSS = val.Shear_ST[0] + aa[(10,7)].subs(s,Length(new_dir,[10,7])) + \
					aa[(11,7)].subs(s,Length(new_dir,[11,7]))

	shear_flow_list.append(SSS)

	aa = Shearflow_package(LL,shear_flow_list)
	
#-------------------------------------------------------------------------#	

	

	# print close_profile.get_resultant_Q(new_dir,aa)

	# draw_ShearFlow3D(g,new_dir,Shear_Flow= aa.values(),num_list = LL,Shear_Center =[0,0],\
	# 							axis = 1,gif=0)

#-------------------------------------------------------------------------#

	liss1 = [10,8,1,2,7,10]
	liss2 = [11,7,2,3,6,11]

	qp1 = close_profile.get_mutiCloseCells_Qp(new_dir,aa,liss1,thickness=[],G = [])
	qp2 = close_profile.get_mutiCloseCells_Qp(new_dir,aa,liss2,thickness=[],G = [])

	g1 = close_profile.get_mutiCloseCells_Gt(new_dir,liss1)
	g2 = close_profile.get_mutiCloseCells_Gt(new_dir,liss2)

	print '------------------',qp1,qp2,g1,g2
	A1 = Surround_Area(new_dir ,liss1,basic_point = [-.5,0] )
	A2 = Surround_Area(new_dir ,liss2,basic_point = [.5,0] )
	

	print '------------------'
	m1 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,liss1,basic_point = [-.5,0] )

	m2 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,liss2,basic_point = [.5,0] )

	pp = [0,0]
	m3 = close_profile.get_mutiCloseCells_Moment(new_dir,aa,basic_point = pp )

	print 'mmmmm',m1,m2,m1+m2,m3

	pub_line = Length(new_dir,[7,2])
	aaaa =  close_profile.solve_Qn(area=[2*A1,2*A2],Gt =[[g1,pub_line],[pub_line,g2]],\
											Qp = [qp1,qp2,m3])

	print 'q1,q2,phi\n',aaaa

	ShearCenter = close_profile.get_mutiCloseCells_ShearCenter\
	(area=[2*A1,2*A2],Gt =[[g1,pub_line],[pub_line,g2]],Qp = [qp1,qp2,m3],Q=1)

	print '\n',ShearCenter[2]+pp[0],'\n'


	# print close_profile.get_resultant_Q(new_dir,aa)

	bb = close_profile.update_mutiCloseCells_Shearflow(aa,[10,8,1,2],aaaa[0])
	bb = close_profile.update_mutiCloseCells_Shearflow(bb,[10,7,2],-aaaa[0])
	m1 = close_profile.get_mutiCloseCells_Moment(new_dir,bb,liss1,basic_point = [-.5,0] )
	print m1

	cc = close_profile.update_mutiCloseCells_Shearflow(aa,[11,6,3,2],-aaaa[1])
	cc = close_profile.update_mutiCloseCells_Shearflow(cc,[11,7,2],aaaa[1])
	m2 = close_profile.get_mutiCloseCells_Moment(new_dir,cc,liss2,basic_point = [.5,0] )
	print m2
 
 #-----------------------------------------------------------------------------------------

	ee = close_profile.update_mutiCloseCells_Shearflow(aa,[10,8,1,2],aaaa[0])
	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[10,7,2],-aaaa[0])

	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[11,6,3,2],-aaaa[1])
	ee = close_profile.update_mutiCloseCells_Shearflow(ee,[11,7,2],aaaa[1])
	m3 = close_profile.get_mutiCloseCells_Moment(new_dir,ee,basic_point = [0,0] )
	print 'm3----->',m3

	print close_profile.get_resultant_Q(new_dir,ee)
 	
 	# print ee[(8,1)].subs(s,1)
 	# print ee[(0,1)].subs(s,1)
 	# print ee[(1,2)].subs(s,0)
 	# draw_ShearFlow3D(g,new_dir,Shear_Flow= ee.values(),num_list = LL,Shear_Center =[0,0],\
		# 						axis = 1,gif=1,save=1,name='two_close_cells_out')