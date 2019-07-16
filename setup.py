from setuptools import setup

setup(
   name='list reaggration',
   version='1.0',
   description='list reaggration from S3',
   author='Eric Wang',
   author_email='ericw@shop.com',
   packages=['db', 'env'],  #same as name
   install_requires=['couchbase', 'boto3'], #external packages as dependencies
)