import random
import sys

class node_shell:
	def __init__(self,yi,node_number,time1,time2):

		self.node_number = node_number 
		self.yi = yi


		self.time1=time1
		self.time2=time2




# def connect_nodes(node1, node2):
# 	node1.neighbour_nodes.append(node2)
# 	node2.neighbour_nodes.append(node1)
# 	node1.list_t_minus_1.append((0,0,node2.node_number))
# 	node2.list_t_minus_1.append((0,0,node1.node_number))




def take(arr):
	t = 0
	for k in arr:
		if(k.time2>t):
			t=k.time2
			k1 = k
	return (k1,t)






def form_gml(dep,no_nodes):
	t=0
	t1 = 0
	t2=10
	arr=[]
	depth = dep-1 # actual depth is actually  depth+1, i.e., dep

	connect=[]

	gmlstr = 'Creater "Mukesh :)"\ngraph [\n'

	# to set the no. of nodes 
	no_nodes=no_nodes

	for i in range(1,no_nodes+1):

		# for keeping depth in check
		if(len(arr)==depth):
			k2,t= take(arr)
			connect.append((i,k2.node_number))
			print("this is t2 max",t)
			t2=t+ random.randint(1,10)
			arr=[]
			t1=t
		else:
			t1=random.randint(t1+1,t2)
			t2=t1+ random.randint(1,10)
		print("start time: ",t1,"end time: ",t2)
		k=node_shell(i,i,t1,t2)

		# for gml file
		# gmlstr+="	node [\n		id "+str(k.node_number)+"\n		value "+str(k.yi)+"\n	]\n" 
		gmlstr+="  node [\n    id "+str(i)+"\n    value "+str(i)+"\n  ]\n" 


		# for keeping depth in check
		# and forming connections
		if(len(arr)==0):
			arr.append(k)
		else:
			for k1 in arr:
				if(k1.time2<t1):
					arr.remove(k1)
			for k1 in arr:
				connect.append((i,k1.node_number))
			arr.append(k)

	print(connect)
	print("\n")

	# for gml file
	for k in connect:
		gmlstr+="  edge [\n    source "+str(k[0])+"\n    target "+str(k[1])+"\n  ]\n"
	gmlstr+="]"


	print("\n---------------------------------------------------------\n")
	print(gmlstr)
	
	return gmlstr


def write_interval(gmlstring):
	f=open('interval_gml.gml','w')
	f.write(gmlstring)
	f.close()
if(len(sys.argv)<3):
	print("Usage:\n python3 interval.py depth no_of_nodes")
	sys.exit()

dep = int(sys.argv[1])
no_nodes=int(sys.argv[2])

	
gmlstring = form_gml(dep,no_nodes)
write_interval(gmlstring)


# print(gmlstring)
