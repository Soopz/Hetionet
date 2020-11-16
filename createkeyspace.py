from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
cluster = Cluster(['192.168.0.1', '192.168.0.2']
session = cluster.connect()
session.execute("CREATE KEYSPACE hetionet with REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")
