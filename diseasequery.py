# Jeffrey Chen 
# Big Data - CSCI 49371
# Professor : Lei xie
from cassandra.cluster import Cluster
from cassandra import ReadTimeout
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

disease_id = raw_input("Enter disease id:")
disease_id = str(disease_id)
name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
result = session.execute(name_look_up,(disease_id,))

print("disease name:")
for x in result:
	print x.name
metaedge = "DlA"
edge_anatomy_look_up = session.prepare('select target from hetionet.edgesbysource where source = ? and metaedge = ? allow filtering')
result = session.execute(edge_anatomy_look_up,(disease_id,metaedge))
print("\n")
print("Disease occurrence:")
for i in result:
	node_id = i.target
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name
print("\n")	

metaedge = "DaG"
edge_gene_look_up = session.prepare('select target from hetionet.edgesbysource where source = ? and metaedge = ? allow filtering')
result = session.execute(edge_anatomy_look_up,(disease_id,metaedge))
print("\n")
print("Disease associates gene:")
for i in result:
	node_id = i.target
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name

print("\n")	

metaedge = "DuG"
edge_gene_look_up = session.prepare('select target from hetionet.edgesbysource where source = ? and metaedge = ? allow filtering')
result = session.execute(edge_anatomy_look_up,(disease_id,metaedge))
print("\n")
print("Disease upregulate gene:")
for i in result:
	node_id = i.target
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name

print("\n")

metaedge = "DdG"
edge_gene_look_up = session.prepare('select target from hetionet.edgesbysource where source = ? and metaedge = ? allow filtering')
result = session.execute(edge_anatomy_look_up,(disease_id,metaedge))
print("\n")
print("Disease downregulate gene:")
for i in result:
	node_id = i.target
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name

print("\n")

metaedge = "CtD"
edge_look_up = session.prepare('select source from hetionet.edgesbytarget where target = ? and metaedge = ? allow filtering')
result = session.execute(edge_look_up,(disease_id,metaedge))
print("\n")
print("Compounds that can treat:")
for i in result:
	node_id = i.source
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name

print("\n")

metaedge = "CpD"
edge_look_up = session.prepare('select source from hetionet.edgesbytarget where target = ? and metaedge = ? allow filtering')
result = session.execute(edge_look_up,(disease_id,metaedge))
print("\n")
print("Compounds that can palliate:")
for i in result:
	node_id = i.source
	name_look_up = session.prepare('select name from hetionet.nodesbyid where id = ?')
	look_up_result = session.execute(name_look_up,(node_id,))
	for j in look_up_result:
		print j.name


