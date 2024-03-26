import boto3
from botocore.client import Config
from  src import config 

def add(name,data):
    try:
        session = boto3.Session(
            aws_access_key_id=config.AWS_ACCESS_KEY,
            aws_secret_access_key=config.AWS_SECRET_KEY,
        )

        # session = boto3.session.Session(region_name='eu-west-2')
        # s3client = session.client('s3', config= boto3.session.Config(signature_version='s3v4'))

        s3 = session.resource("s3", config=Config(signature_version='s3v4'))
        print(config.AWS_SECRET_KEY)
        bucket = s3.Bucket(config.S3_BUCKET_NAME,)

        object = bucket.put_object(Key=name, Body=data)

        print(object)
        return object
    except Exception as e:
    
        return None

def get_url(name):
    try:
        session = boto3.Session(
            aws_access_key_id=config.AWS_ACCESS_KEY,
            aws_secret_access_key=config.AWS_SECRET_KEY,
        )

        s3 = session.resource("s3", config=Config(signature_version="s3v4",region_name="eu-west-2"))
        return s3.meta.client.generate_presigned_url(
            "get_object", Params={"Bucket": config.S3_BUCKET_NAME, "Key": name}, ExpiresIn=86400
        )
        
        return presigned_url
    except Exception as e:
        return e



def create_name():
    pass