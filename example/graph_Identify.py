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
	# val = read_exe.Read_COS('/home/eacaen/TUBS_graduation/draft/test_data/[]2.xlsx')	
	val = read_exe.Read_COS('../test_data/shape4.xlsx')	

	lis = val.cos_value	
 	dirddd =cos_To_dict(lis)

	g = Graph()
	for i in range(len(dirddd)):
		g.addVertex(i)

	for i in range(len(dirddd)-1):
		g.addEdge(i,i+1,0.1)

 	print dirddd
 	print dirddd.items()
 	def cos_to_dir(cos,dir):
 		for i,j in dir.items():
 			if cos == j:
 				return i
 		return None

 	def ccc(cos_value,dir):
 		pass
	 # 	try:
	 # 		return dict.keys()[dict.values().index(value)]
		# except ValueError:
	 #    	pass
	ccc = ([(((-1, -1), (0, -1)), 0.219669914110089*s*t - 0.0909902576697319*t*(0.5*s**2 - s)), \
		    (((0, -1), (1, -1)), -0.045495128834866*s**2*t + 0.219669914110089*s*t + 0.265165042944955*t),\
		    (((1, -1), (-1, 1)), -0.0909902576697319*t*(-0.353553390593274*s**2 + s) - 0.219669914110089*t*(0.353553390593274*s**2 - s) + 0.439339828220179*t)\
		  ])
	print cos_to_dir([-1.0, -0.1],dirddd)
	print cos_to_dir([-1.0, -1.0],dirddd)
	print ccc[0]
	print ccc[0][0]
	print ccc[0][0][0]
	print len(ccc)