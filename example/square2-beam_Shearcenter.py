#coding:utf-8
import sys
sys.path.insert(0, "../source")
import read_exe
import profile
import open_profile
import close_profile
from graph import *
from graph_plugin import *
from profile_plugin import *
import profile_toolbox

if __name__ == "__main__":	
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/square2.xlsx')	
 	
	lis = val.cos_value	
	# lis.reverse()
	# print lis
	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,1)
 

	# g.ChangeWeight(0,1,2)
	# g.ChangeWeight(4,5,2)


	# draw_point_graph(g,dirddd,color='b')

	thk = graph_line_thickness(g,range(len(lis)))
	print '--------------------------',thk
	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)
 
	new_dir = Pc.profile_To_centriod()
 
	# draw_point_graph(g,Pc.dir ,color='b')
	cccc = dict_To_cos(Pc.dir)


	cc = open_profile.Open_Profile(cccc,Pc,thickness=thk,Qx =0,Qy =1)

 	print 'cos_value-->',cc.cos_value
	# print 'length-->',cc.length
	# print 'Ix-->',cc.Ix
	# print 'Iy-->',cc.Iy
	# print 'Ixy-->',cc.Ixy
	# print 'Sx-->',cc.Sx
	# print 'Sy-->-->',cc.Sy
	# print 'Shear_ST-->',cc.Shear_ST
	
	A = open_profile.Surround_Area(cc.cos_value,basic_point = [-1,0])

	# Q0 = open_profile.get_Shear_Qo(cc.Shear_ST, cc.cos_value)/ (2*A)
	# print Q0

	# Shear_ST = [x + Q0 for x in cc.Shear_ST]

	pp = [-0.4,-0.646]
	a = -.5
	b = -.5
	for i in range(20):
		a = a + 0.1/2
		b = -1
		for j in range(20):
			b = b + 0.1/2
			pp = [a,b]
			if  profile_toolbox.is_point_in(pp, cccc):


			 	Cxy = close_profile.close_Shear_center(cccc, Pc,thickness = thk ,basic_point = pp)
			 	print 'Cxy',Cxy

		 	# Sxy = open_profile.get_Shear_center(cccc, Pc,thickness = thk ,basic_point = pp)
		 	# print Sxy
 


	# draw_ShearFlow(Shear_ST,val.length)
	# lin = line_value_package([0,1,2,3,4,5])
	# draw_ShearFlow3D(g,dirddd,val.Shear_ST,lin, axis = 1)

