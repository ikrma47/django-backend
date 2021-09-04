from django.conf import settings
from random import randint
import logging
import boto3
from botocore.exceptions import ClientError

def generateOtp():
    return randint(1000,9999)




def create_presigned_url(object_name, bucket_name=settings.BUCKET_NAME,
                        fields=None, conditions=None, expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file
    
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                    object_name,
                                                    Fields=fields,
                                                    Conditions=conditions,
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response