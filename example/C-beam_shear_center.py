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
	lis = copy.copy(val.cos_value)
	# lis.reverse()
	print lis
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1, 1)
 
	thk = graph_line_thickness(g,range(len(lis)))
	print '--------------------------',thk
	# draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	new_dir = Pc.profile_To_centriod()

	cccc = dict_To_cos(new_dir)
 	print 'ccccc--->',cccc ,'\n\n'

	
	a = -0.8
	b = -1
	for i in range(10):

		a = a + 0.1
		b = -1
		for j in range(10):
			b = b + 0.2
			pp = [a,b]

			# print '\n\n',pp
			# c_x = copy.copy(cccc)
			# k = open_profile.if_clockwise(c_x)
			# if k > 0:
			# 	c_x.reverse()

 		# 	cc = open_profile.Open_Profile(c_x,Pc,thickness = thk,Qx = 0,Qy = 1)
			# xx = open_profile.get_Shear_center_x(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
 		# 	# print xx+ pp[0] 			


 		# 	c_y = copy.copy(cccc)
			# k = open_profile.if_clockwise(c_y)
			# if k < 0:
			# 	c_y.reverse()
			# dd = open_profile.Open_Profile(c_y,Pc,thickness = thk,Qx =1,Qy = 0)
			# yy = open_profile.get_Shear_center_y(dd,Shear_ST = dd.Shear_ST,basic_point = pp)
 		# 	print xx+ pp[0] , '   ' ,yy+ pp[1] 
 			
 			Sxy = open_profile.get_Shear_center(cccc, Pc,thickness = thk ,basic_point = pp)
 			print Sxy

 			

			# print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST)
	# open_profile.get_circle(cccc,Shear_ST = Shear_ST )

 	# cc.report()