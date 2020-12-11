
from my_set import *
#from interval import * as interval


BETA = 0.0001
Q = 30000
import sys

COFFECIENT = 1000000

IS_TREE=False

class node:
	def __init__(self,yi,node_number,total_nodes):
		self.neighbour_nodes = []
		self.node_number = node_number 
		self.yi = yi
		self.xi = yi
		self.total_nodes = total_nodes
		self.list_t_minus_1 = []
		self.has_completed = False

		self.list_t =[]



	def send_message(self):
		for neighbour_node in (self.neighbour_nodes):
			value = self.yi
			cardinality = 1

			#calculate mean and cardinality for each neighbour
			for message in self.list_t_minus_1:
				if(neighbour_node.node_number!=message[2]):

					value = value+ message[0]*message[1]
					cardinality = cardinality + message[1]


			#modifying cardinality
			mean = value/cardinality
			if not IS_TREE:
				cardinality = cardinality/(1+(1/Q*BETA)*cardinality)
		
			sending_tuple = (mean,cardinality,self.node_number)


			#send sending_tuple to each neighbour node
			neighbour_node.list_t.append(sending_tuple)

	def calculate_xi(self):
		# if(self.has_completed):
		# 	return
		summation = self.yi
		cardinality = 1
		# print("",end=" | {'1',")
		for message in self.list_t:
			summation = summation + message[0]*message[1]
			cardinality = cardinality + message[1]
			# print("hi ",end=" ")
		# print(" ")
			# print(message[1],end=",")

		# print("}", end ="")

		
		# print("cardinality of {} is {}".format(self.node_number,cardinality))
		before_value = self.xi
		try:
			if(abs(before_value-(summation/cardinality))<0.001):
				self.has_completed = True
		except Exception:
			print("before value: ",before_value)
			print("summation :",summation)
			print("cardinality",cardinality)
			sys.exit()
		
		# to do may be summation can change after next iteration of t where has_completed = true
		self.xi = summation/cardinality
		# print("cardinality is ",cardinality)

		self.list_t_minus_1 = self.list_t.copy()
		self.list_t = []






def connect_nodes(node1, node2):
	node1.neighbour_nodes.append(node2)
	node2.neighbour_nodes.append(node1)
	node1.list_t_minus_1.append((0,0,node2.node_number))
	node2.list_t_minus_1.append((0,0,node1.node_number))
	





def run_simulation(list_of_all_nodes,is_tree=False,print_every=100000):
	global IS_TREE

	IS_TREE = is_tree
	###########print("\n\n")

	count = 0
	while True:
	#for i in range(0,20000):
		count = count +1
		for k in list_of_all_nodes.values():
			k.send_message()


		for k in list_of_all_nodes.values():
			k.calculate_xi()
			if(count%print_every==0):
				print(" | {:^4}".format(k.xi),end = '')
				print("",end="")
		if(count%print_every==0):
			print(" |\n "+"-"*106)


		shouldrun = False
		for k in list_of_all_nodes.values():
			if not (k.has_completed):
				shouldrun = True

		if(not shouldrun):
			break

	for k in list_of_all_nodes.values():
		# k.calculate_xi()
		print(" | {:^18}".format(k.xi),end = '')
		print("",end="")



	print("\nTotal iterations = {}".format(count-1))

# print()






def make_graph(edges,nodes):
	output_nodes = {}


	for node_id in nodes:
		output_nodes[node_id]=(node(node_id,node_id,0))


	for edge in edges:
	
		value1 = int(edge[0])
		value2 = int(edge[1])
		if(not (output_nodes[value1] in output_nodes[value2].neighbour_nodes)):
			connect_nodes(output_nodes[value1],output_nodes[value2])


	return output_nodes



# checking the no. of arguments provided from terminal should suffice the need
if(len(sys.argv)<3):
	print("Usage:\n python3 consensus.py <gml_file> <graph/tree>\n")
	print("Example:\n python3 consensus.py interval_gml.gml graph")
	sys.exit()




#------------------- GML file containing graph----------------------

gml_file = str(sys.argv[1])

#------------------------------------------------------------------

# give_spanning_tree    --------- result spanning tree 
# give_graph 			--------- return normal graph
# give_connected_graph  --------- reture you a manually connected graph
# Also-----
# passed = True if you want to simulate tree's algo
# passed = False if you want to simulate general graphs algo


algo = str(sys.argv[2])
if(algo == "tree"):
	edges, nodes = give_spanning_tree(gml_file)
	passed = True
elif(algo == "graph"):
	edges, nodes = give_connected_graph(gml_file)
	passed = False
else:
	print("The last argument can take either---\n   1) tree \n   2) graph")
	sys.exit()



# edges, nodes = give_graph(gml_file)

# OR (this needs making some additional tweaks)
#file_str = form_gml(4,10) # (depth,no_nodes)
#edges, nodes = give_connected_graph_from_str(file_str)
#edges, nodes = give_spanning_tree_from_str(file_str)

#-------------------------------------------------------------------


list_of_all_nodes = make_graph(edges,nodes)

original_values = [x.yi for x in list_of_all_nodes.values()]

original_mean = sum(original_values)/len(original_values)


#-----------------------------------------------------------------

run_simulation(list_of_all_nodes,passed)

#--------------------------------------------------------------------

squared_error = [(x.xi-original_mean)**2 for x in list_of_all_nodes.values()]
 
standard_deviation = (sum(squared_error)/len(original_values))**(1/2)

# Reporting output in a file
stri = "total nodes : {}, standard_deviation : {}\n".format(len(original_values),standard_deviation)
y = open("details.txt","a")
y.write(stri)



