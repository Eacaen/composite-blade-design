from shear_stream import *
from read_exe import *
from profile import *
if __name__ == "__main__":

	xy = [[-1,-1],[0,-1],[1,-1],[-1,1],[0,1],[1,1]]
	read_exe.draw_points(xy)
	# val = Read_COS('../test_data/gong_1.xlsx')
	# read_exe.draw_points(val.cos_value)