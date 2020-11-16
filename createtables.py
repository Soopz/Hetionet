from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute('create table "hetionet"."nodesbyid"("id" ascii,"name" ascii,"kind" ascii,PRIMARY KEY("id"))' )
session.execute('create table "hetionet"."nodesbyname"("id" ascii,"name" ascii,"kind" ascii,PRIMARY KEY("name"))' )
session.execute('create table "hetionet"."edgesbysource"("source" ascii,"metaedge" ascii,"target" ascii,PRIMARY KEY("metaedge","source"))' )
session.execute('create table "hetionet"."edgesbytarget"("source" ascii,"metaedge" ascii,"target" ascii,PRIMARY KEY("target","metaedge"))' )
