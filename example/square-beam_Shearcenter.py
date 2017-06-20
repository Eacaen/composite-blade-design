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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/square.xlsx')	
	lis = val.cos_value	
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1, 1)
 
	# draw_point_graph(g,dirddd,color='b')

	thk = graph_line_thickness(g,[0,1,2,3,4])
	print '--------------------------',thk
	# draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	new_dir = Pc.profile_To_centriod()

	cccc = dict_To_cos(new_dir)
	# cccc = lis
	print 'ccccc--->',cccc ,'\n\n'

	pp = [0,0]
	cc = open_profile.Open_Profile(cccc,Pc,Qx = 0,Qy = 1,thickness = thk)
	xx = open_profile.get_Shear_center_x(cc,cccc,Shear_ST = cc.Shear_ST ,basic_point = pp)

	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]
	print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)


	cc = open_profile.Open_Profile(cccc,Pc ,Qx = 1,Qy = 0,thickness = thk)
	yy = open_profile.get_Shear_center_y(cc,cccc,Shear_ST = cc.Shear_ST ,basic_point = pp)

	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 
	

	print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)

	open_profile.get_circle(cccc,Shear_ST = cc.Shear_ST)

	# pp = [2,1]
	# cc = open_profile.Open_Profile(cccc,Pc,Qx = 0,Qy = 1,thickness = thk)
	# xx = open_profile.get_Shear_center_x(cc ,cccc,basic_point = pp)
	# yy = open_profile.get_Shear_center_y(cc ,cccc,basic_point = pp)
 # 	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]

 # 	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 	

 	# cc.report()