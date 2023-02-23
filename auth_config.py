from collections import namedtuple

import boto3
from botocore.exceptions import ClientError
import json


def custom_object_converter(object_dic: dict):
    return namedtuple('X', object_dic.keys())(*object_dic.values())


def get_secret():

    secret_name = "dev/fastapi/postgres"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return json.loads(secret, object_hook=custom_object_converter)