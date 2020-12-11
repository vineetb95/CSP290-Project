import os
import time

# this file is exclusively for interval grphas' gml file.
interval_gml_file = "interval_gml.gml"
algo = "graph"


def give_graph(depth,interval_gml_file,algo):

	timestr = "Executed at GMT time: {}:{}:{} {}-{}-{}\n".format(time.gmtime().tm_hour ,time.gmtime().tm_min ,time.gmtime().tm_sec ,time.gmtime().tm_mday ,time.gmtime().tm_mon ,time.gmtime().tm_year)
	stri = timestr
	y = open("details.txt","a")
	stri += "GML File used: {} ------&-------Algorithm used: {}\n".format(interval_gml_file,algo)
	stri += "Follwing records are for depth {} of interval graph\n\n".format(depth) 
	y.write(stri)
	y.close()
	for k in range(1,21):
		stri = "python3 interval.py {} {}".format(depth, 50*k)
		stri2 = "python3 consensus.py {} {}".format(interval_gml_file,algo)

		os.system(stri)
		os.system(stri2)
	y = open("details.txt","a")
	y.write("\n.............................................\n\n")



give_graph(3,interval_gml_file,algo)
give_graph(4,interval_gml_file,algo)
