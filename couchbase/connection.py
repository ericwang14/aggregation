import couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from reaggregation.env.main import env

#connect and return the cluster connection
def connect():
	host_name = env.get_host_name()
	bucket = env.get_bucket_name()
	password = env.get_bucket_password()

	cluster = Cluster("couchbase://" + host_name + "?operation_timeout=60")
	authenticator = PasswordAuthenticator(bucket, password)
	cluster.authenticate(authenticator)

	return cluster.open_bucket(bucket)


# if __name__ == '__main__':
# 	connect()


