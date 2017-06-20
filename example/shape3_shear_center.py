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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/shape3.xlsx')	
	lis = val.cos_value
	lis.reverse()
	# print lis
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1, 1)
 
	thk = graph_line_thickness(g,range(len(lis)))
	print '--------------------------',thk
	draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	new_dir = Pc.profile_To_centriod()

	cccc = dict_To_cos(new_dir)
 
 	print 'ccccc--->',cccc ,'\n\n'

	
	a = -1
	b = -1
	for i in range(15):

		a = a + 0.1
		b = -1
		for j in range(20):
			b = b + 0.1
			pp = [a,b]

			
			# cc = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
			# xx = open_profile.get_Shear_center_x(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
 		# 	print  xx+ pp[0]

 			# print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0] 
 			
 			# print '\n\n',pp
			# cc = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 1,Qy = 0)
			# yy = open_profile.get_Shear_center_y(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
			# print yy+ pp[1]
  			# print 'yyyyyyy--->',yy,yy-pp[1],yy+ pp[1],'\n\n'

 			Sxy = open_profile.get_Shear_center(cccc, Pc,thickness = thk ,basic_point = pp)
 			print Sxy

	# print '\n',open_profile.get_resultant_Qx(cccc,Shear_ST = cc.Shear_ST)
	# open_profile.get_circle(cccc,Shear_ST = Shear_ST )

 	# cc.report()