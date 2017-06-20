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
	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/square_middle.xlsx')	
	lis = val.cos_value	
	lis.reverse()
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1, 1)

 
	# g.ChangeWeight(0,1,0.001)
	# g.ChangeWeight(4,5,0.001)

	thk = graph_line_thickness(g,[0,1,2,3,4,5])
	print '--------------------------',thk
	# draw_point_graph(g,dirddd,color='b')


	Pc = Profile_Constant(thickness = thk,graph = g,dir = dirddd)

	new_dir = Pc.profile_To_centriod()

	cccc = dict_To_cos(new_dir)
	# cccc = lis
	print 'ccccc--->',cccc ,'\n\n'

	pp = [-0.4254235,-.4324245]
	cc = open_profile.Open_Profile(cccc,Pc,thickness = thk,Qx = 0,Qy = 1)
	A = open_profile.Surround_Area(cc.cos_value,basic_point = [-1,0])
	Q0 = open_profile.get_Shear_Qo(cc.Shear_ST,cccc,basic_point =[0,0]) / (2*A)
	# print 'QQQ----[[[-*',Q0
	Shear_ST = [x - Q0 for x in cc.Shear_ST]
	xx = open_profile.get_Shear_center_x(cc,Shear_ST = Shear_ST,basic_point = pp)
	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]


	cc = open_profile.Open_Profile(cccc,Pc ,thickness = thk,Qx = 1,Qy = 0)
	Q0 = open_profile.get_Shear_Qo(cc.Shear_ST,cccc,basic_point =[0,0]) / (2*A)
	# print 'QQQ----[[[-*',Q0
	Shear_ST = [x - Q0 for x in cc.Shear_ST]
	yy = open_profile.get_Shear_center_y(cc,Shear_ST = Shear_ST,basic_point = pp)
	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 

	# print '\n',open_profile.get_resultant_Q(cccc,Shear_ST = cc.Shear_ST,thickness = thk)

	# pp = [2,1]
	# cc = open_profile.Open_Profile(cccc,Pc,Qx = 0,Qy = 1,thickness = thk)
	# xx = open_profile.get_Shear_center_x(cc ,basic_point = pp)
	# yy = open_profile.get_Shear_center_y(cc ,basic_point = pp)
 # 	print 'xxxxxx--->\n',xx,xx-pp[0],xx+ pp[0]

 # 	print 'yyyyyyy--->\n',yy,yy-pp[1],yy+ pp[1] 	

 	# cc.report()