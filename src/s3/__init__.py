import boto3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

s3_resource = boto3.resource(
    's3',
    aws_access_key_id=config['AWS']['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=config['AWS']['AWS_SECRET_ACCESS_KEY'])