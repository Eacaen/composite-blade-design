#coding:utf-8
#############################################################################
# move C-beam to its Centroid
# get its engineer constant value
# plot it out
#############################################################################

import sys
sys.path.insert(0, "../source")
import read_exe
from shear_stream import *
import profile 
from graph_plugin import *

if __name__ == "__main__":	

	val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[.xlsx')
	lis = val.cos_value	
	tk = np.ones(len(lis))

	val = Profile_Constant(lis,tk)

	print val.__doc__
	print val.cos_value
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	
	print 'cent',Find_Centroid(val.cos_value,area  = val.Area)

	read_exe.draw_points(val.cos_value,color='b')
	print 'after -----------------------------------------------'

	print val.profile_To_centriod()
	print val.__doc__
	print val.Ix
	print val.Iy
	print val.Ixy
	print val.Area
	print 'cent',Find_Centroid(val.cos_value,area  = val.Area)
	# read_exe.draw_points(lis)
	read_exe.draw_points(val.cos_value,color='b')