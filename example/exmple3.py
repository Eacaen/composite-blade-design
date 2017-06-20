# Example 2 page 39 from "Basic Mechanics of Laminated Composite Plates" # A.T. Nettles # NASA Reference Publication 1351
import sys
sys.path.insert(0, "../source")
from laminate_Tools import *
import matplotlib.pyplot as plt
import matplotlib
#the chinese book example P31
if __name__ == "__main__":
	max_load_list = []
	load_strain = []

	a = Lamina(E1=2001.0, E2=1301.0, G12=1001.0,v21 = 0.3,angle = 0,thickness=1)

	b = Lamina(E1=2001.0, E2=1301.0, G12=1001.0,v21 = 0.3,angle = 45,thickness=10)

 	c = Lamina(E1=2001.0, E2=1301.0, G12=1001.0,v21 = 0.3,angle = 70,thickness=1)


	LAA = Laminate()
	LAA.add_Lamina(a)
	LAA.add_Lamina(b)	
	LAA.add_Lamina(c) 
	LAA.update()

	print '----A-----\n\n',LAA.A
	print '\n\n------B------\n\n',LAA.B
	print '\n\n------D------\n\n',LAA.D
	print LAA.Qk

