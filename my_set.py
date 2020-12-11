

class parser():
	def __init__(self,stri):

		self.stri = " ".join(stri.split("\n"))


	def get_word(self,start):
		
		while(start<len(self.stri) and self.stri[start]==" "):
			start=start+1
		word = ""
		if (start<len(self.stri) and self.stri[start]=="\""):
			start=start+1
			
			while(start<len(self.stri) and self.stri[start]!="\""):
				word = word + self.stri[start]
				start = start+1

			start = start+1
				
		else:
			while(start<len(self.stri) and self.stri[start]!=" "):
				word = word + self.stri[start]
				start = start+1

		
		return start,word

	def get_key_value(self,count):

		count,key = self.get_word(count)
		count,value = self.get_word(count)
		
		return count, key, value

		
	def parse_node(self,count):

		
		count,_ =self.get_word(count) #[
		
		node_dict={}
		while(self.get_word(count)[1]!="]"):
			count,key,value = self.get_key_value(count)
			node_dict[key]= value

		count,_ = self.get_word(count)
		return count,node_dict


	def parse_graph(self):
		count = 0
		word = ""
		

		while(word!="node"):
			count,word = self.get_word(count)
			

		

		lis_nodes =[]
		
		count,dic= self.parse_node(count)
		
		lis_nodes.append(int(dic["id"]))
		count,word = self.get_word(count)

		

		while(word=="node"):
			count,dic = self.parse_node(count)
			lis_nodes.append(int(dic["id"]))
			
			count,word = self.get_word(count)


		edges = []
		while(count<len(self.stri) and word=="edge"):
			count,dic = self.parse_node(count)
			edges.append((int(dic["source"]),int(dic["target"])))
			count,word = self.get_word(count)

		
		return edges,lis_nodes

















list_of_edges=[]
class set1():
	def __init__(self,value):
		self.value = value
		self.parent = self
		self.is_parent = True
		
	def get_parent(self):
		x = self
		while(not x.is_parent):
			x = x.parent
		return x

	def union(self,other_set):
		p1 = self.get_parent()
		p2 = other_set.get_parent()

		if(p1!=p2):
			p1.parent = p2
			p1.is_parent = False
			list_of_edges.append((self.value,other_set.value))




def give_graph(file_name):
	y = open(file_name)
	u = y.read()
	y.close()
	v= parser(u)
	edges,lis_nodes = v.parse_graph()

	return edges,lis_nodes



def give_connected_graph(file_name):
	y = open(file_name)
	u = y.read()
	y.close()
	v= parser(u)
	edges,lis_nodes = v.parse_graph()

	print("done parsing")

	nodes = {}
	for k in lis_nodes:
		nodes[k] = set1(k)

	for k in edges:
		nodes[k[0]].union(nodes[k[1]])

	paren1 = nodes[1].get_parent().value

	for k in nodes.values():
		if (k.get_parent().value!=paren1):
			edges.append((paren1,k.parent.value))
			print("Graph is not connected \n Connecting manually")

	return edges,lis_nodes


def give_spanning_tree(file_name):
	y = open(file_name)
	u = y.read()
	y.close()
	v= parser(u)
	edges,lis_nodes = v.parse_graph()

	print("done parsing")

	nodes = {}
	for k in lis_nodes:
		nodes[k] = set1(k)

	for k in edges:
		nodes[k[0]].union(nodes[k[1]])

	paren1 = nodes[1].get_parent().value

	for k in nodes.values():
		if (k.get_parent().value!=paren1):
			list_of_edges.append((paren1,k.parent.value))
			print("Graph is not connected \n Connecting manually")

	return list_of_edges,lis_nodes



##############################################################33

def give_connected_graph_from_str(file_str):
	#y = open(file_name)
	#u = y.read()
	#y.close()
	v= parser(file_str)
	edges,lis_nodes = v.parse_graph()

	print("done parsing")

	nodes = {}
	for k in lis_nodes:
		nodes[k] = set1(k)

	for k in edges:
		nodes[k[0]].union(nodes[k[1]])

	paren1 = nodes[1].get_parent().value

	for k in nodes.values():
		if (k.get_parent().value!=paren1):
			edges.append((paren1,k.parent.value))
			print("Graph is not connected \n Connecting manually")

	return edges,lis_nodes


def give_spanning_tree_from_str(file_str):
	#y = open(file_name)
	#u = y.read()
	#y.close()
	v= parser(file_str)
	edges,lis_nodes = v.parse_graph()

	print("done parsing")

	nodes = {}
	for k in lis_nodes:
		nodes[k] = set1(k)

	for k in edges:
		nodes[k[0]].union(nodes[k[1]])

	paren1 = nodes[1].get_parent().value

	for k in nodes.values():
		if (k.get_parent().value!=paren1):
			list_of_edges.append((paren1,k.parent.value))
			print("Graph is not connected \n Connecting manually")

	return list_of_edges,lis_nodes


