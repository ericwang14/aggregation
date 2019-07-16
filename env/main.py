#!/bin/python

'''
environment config, default environment will be dev
use SHOPENV to change the environment variable
'''
assert(__name__ != '__main__')

DEFAULT_ENV = 'dev'

main_env = DEFAULT_ENV

s3_buckets = {
    'dev': 'shopma-hummingbird-dev',
    'staging': 'shopma-hummingbird-staging',
    'production': 'shopma-hummingbrid'
}

dev_host_name = "cbcloud-ds01.maeagle.corp:8091,cbcloud-ds02.maeagle.corp:8091,cbcloud-ds03.maeagle.corp:8091"
dev_bucket_name = "pipeline_dev"
dev_bucket_password = "p1p3l1n3!"

staging_host_name = "cbcloud-ds01.maeagle.corp:8091,cbcloud-ds02.maeagle.corp:8091,cbcloud-ds03.maeagle.corp:8091"
staging_bucket_name = "pipeline_stage"
staging_bucket_password = "p1p3l1n3!"

production_host_name = "cbcloud-p01.maeagle.corp:8091,cbcloud-p02.maeagle.corp:8091,cbcloud-p03.maeagle.corp:8091"
production_bucket_name = "pipeline"
production_bucket_password = "p1p3l1n3!"

def change_env(env):
    main_env = env;

def get_env():
    return main_env


def get_s3_bucket():
    return s3_buckets.get(main_env, None)


def get_host_name():
	switcher = {
		'dev': dev_host_name,
		'staging': staging_host_name,
		"production": production_host_name
	}

	return switcher.get(main_env, None)

def get_bucket_name():
	switcher = {
		'dev': dev_bucket_name,
		'staging': staging_bucket_name,
		"production": production_bucket_name
	}

	return switcher.get(main_env, None)

def get_bucket_password():
	switcher = {
		'dev': dev_bucket_password,
		'staging': staging_bucket_password,
		"production": production_bucket_password
	}

	return switcher.get(main_env, None)
