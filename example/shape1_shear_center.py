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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/shape1.xlsx')	
	lis = val.cos_value
	# lis.reverse()
	print lis
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1, 1)
 
	thk = graph_line_thickness(g,[0,1,2,3,4,5])
	print '--------------------------',thk
	# draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	new_dir = Pc.profile_To_centriod()

	cccc = dict_To_cos(new_dir)

	print 'ccccc--->',cccc ,'\n\n'

	pp = [-0.94,-0.9]
	# a = -2
	# b = -1.5
	# for i in range(40):
	# 	a = a + 0.1
	# 	b = -2
	# 	for j in range(40):
	# b = b + 0.1
	# pp = [a,b]
	cc = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = -1)
	xx = open_profile.get_Shear_center_x(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0] 
	print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)



	cc = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx =1,Qy = 0)
	yy = open_profile.get_Shear_center_y(cc,Shear_ST = cc.Shear_ST,basic_point = pp)
	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 

	print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)
	# open_profile.get_circle(cccc,Shear_ST = Shear_ST )

 	# cc.report()