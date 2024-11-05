import logging
import boto3
import botocore

def handler(event, context):
    aws_access_key_id = 'Key Id'
    aws_secret_access_key = 'Secret Key'
    endpoint = 'https://storage.yandexcloud.net'
    success_link = 'https://sample-darkhhh-bucket.website.yandexcloud.net/'
    # 60 seconds * 60 = 60 minutes
    # 60 minutes * 24 = 24 hours = 1 day
    policy_expire_in = 60 * 60 * 24 * 7

    s3 = boto3.client('s3',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name='ru-central1',
                    endpoint_url=endpoint,
                    config=botocore.client.Config(signature_version='s3v4'),
                    )
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    key = 'users/uploads/${filename}'
    bucket = 'sample-darkhhh-bucket'
    conditions = [{"acl":"public-read"}, ["starts-with", "$key", "users/uploads"], {'success_action_redirect': success_link}]
    fields = {'success_action_redirect': success_link}

    prepared_form_fields = s3.generate_presigned_post(Bucket=bucket,
                                                    Key=key,
                                                    Conditions=conditions,
                                                    Fields=fields,
                                                    ExpiresIn=policy_expire_in)

    logger.info(prepared_form_fields)