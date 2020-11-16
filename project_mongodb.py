#Author: Nelson Lim
#CSCI 493.71
#April 5, 2020
from pymongo import MongoClient
client = MongoClient("mongodb+srv://nelson:1122334455@project1-6eqsx.mongodb.net/test?retryWrites=true&w=majority")
db = client.hetio

#Assumes that the user is only entering one disease with multiple relationships to different genes
inpt = input("How many Relationship(s) does this new disease have? ")
new_Disease = input("Enter new diease ID: ")

for i in range(int(inpt)):
	meta = input("Enter metaedge ID (DaG, DuG, DdG): ")
	gen = input("Enter affected gene ID: ")
	db.edges.insert_one({"source": str(new_Disease), "metaedge": str(meta),  "target": str(gen)})

#Dictionary for containing the different genes the Disease affected
gene = []
#Finds the target genes for the new disease we entered 
mydoc = db.edges.find({'source':new_Disease, 'metaedge':{"$in": ["DaG","DuG","DdG"]}}, {'_id': False, 'target': True})
for x in mydoc:
	gene.append(x["target"])
#Dictionary for storing compounds
nam = []
slr = []
for gene in gene:
	#print(gene) #Prints gene names
	treat = db.edges.find({"metaedge": {"$in": ["CuG", "CdG"]}, "target": str(gene)} , {'_id': False, 'source': True})
	for y in treat:
		#print(y["source"]) #print compound names
		nam = (str(y["source"]))
		slr.append((str(y["source"])))
		#convert compounds ID to names
		name = db.nodes.find_one({"id": nam},{'_id':False, 'name':True})
		print(name["name"])

		#related drugs
		#print(nam)

print("Related compounds: ")

for slr in slr:
	sim = db.edges.find({"source":slr, "metaedge":"CrC"})
	for h in sim:
		#print(str(h["target"]))
		u = (str(h["target"]))
		print(u)
