from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
# ssl_context = SSLContext(PROTOCOL_TLSv1)
# ssl_context.load_verify_locations('/Users/superpoots/AmazonRootCA1.pem')
# ssl_context.verify_mode = CERT_REQUIRED
# auth_provider = PlainTextAuthProvider(username='jc5555-at-519708134265', password='J71Pi8sPF8x0I+eRlwXAWtSsszwD3+oLeipC1gH+sJc=')
cluster = Cluster(['192.168.0.1', '192.168.0.2']
session = cluster.connect()
session.execute("CREATE KEYSPACE hetionet with REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")