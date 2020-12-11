# Point to note---
	/ Each node has a unique identification namely--- node_id.
	/ Each node contains some value, the mean of which needs to be calculated.
	/ For convinience, we have taken value = node_id, for each such node.
	/ So, if no.of_nodes = 1000 nodes(that is node_id varies from 1 to 1000)
	/ Then, value contained in node will also vary from 1,2,3,4,5.....,998,999,1000.
	/ Hence, in this particular example 
		mean = summation(1 to 1000)/1000
		     = 500.5



1) consensus.py contains the main algorithm. 2 configurable things in this file.
	Usage:
		python3 consensus.py <gml_file> <graph/tree>
	Example:
		python3 consensus.py interval_gml graph
	Explanation:
		<graph> means using graph algorithm
		<tree> means using tree algorithm

2) interval.py is used to generate a gml file for interval graph (generated_file_name="interval_gml.gml")
	Usage:
		python3 interval.py <depth> <no_of_nodes>
	Example:
		python3 interval.py 4 1000
	Suggestion:
		try to keep depth not larger than 10.
	Explanation:
		interval_gml.gml file is completely re-written, every time this command is executed. 

3) my_set.py contains below 3 functions which parse the gml file to return their respective outputs.
	1) give_graph
	2) give_connected_graph
	3) give_spanning_tree

4) make_observation.py is used only for interval_graph cases, to report the trend of
	-- depth vs no.of_nodes
	\ It returns the output in a details.txt file.
	\ Each time you run make_observation.py, output is appended in details.txt file.
	\ To create a completely separate details.txt file, delete the old one first.
	

# Running order-------For making observation only
	/ run make_observaton.py

# Running order----For checking algorithm (each result)
	/ If you already have the gml file run consensus.py directly.
	/ Else first run interval.py to create interval_gml.gml file(interval graph) and then consensus.py

	

