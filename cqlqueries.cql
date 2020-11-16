copy hetionet.nodesbyid (id,name,kind) from 'C:\Users\Pixel\Documents\Big Data Project\nodes.csv' WITH HEADER = True;
copy hetionet.nodesbyname (id,name,kind) from 'C:\Users\Pixel\Documents\Big Data Project\nodes.csv' WITH HEADER = True;
copy hetionet.edgesbysource (source,metaedge,target) from 'C:\Users\Pixel\Documents\Big Data Project\edges.csv' with header = true;
copy hetionet.edgesbytarget (source,metaedge,target) from 'C:\Users\Pixel\Documents\Big Data Project\edges.csv' with header = true;