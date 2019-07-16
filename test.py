#!/bin/python
import boto3
s3_resource = boto3.resource('s3')

for page in s3_resource.Bucket('shopma-hummingbird-dev').\
        objects.filter(Prefix='transactions/lists/v5/shopperlists/raw').pages():
    for obj in page:
        print(obj.key)
