from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import sys
sys.path.append("..")

from env import main

#connect and return the cluster connection
def connect():
	host_name = main.get_host_name()
	bucket = main.get_bucket_name()
	password = main.get_bucket_password()

	cluster = Cluster("couchbase://" + host_name + "?operation_timeout=60")
	authenticator = PasswordAuthenticator(bucket, password)
	cluster.authenticate(authenticator)

	return cluster.open_bucket(bucket)



