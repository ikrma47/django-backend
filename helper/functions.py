from rest_framework.views import exception_handler
from django.conf import settings
from random import randint
import logging
import boto3
from botocore.exceptions import ClientError


def generateOtp():
    return randint(1000, 9999)


def create_presigned_url(
    object_name,
    object_type,
    bucket_name=settings.BUCKET_NAME,
    expiration=3600
):

    # added a random number to file name to have unique file name
    object_name = object_name[:object_name.rfind(
        '.')] + str(generateOtp()) + str(generateOtp()) + object_name[object_name.rfind('.'):]

    """Generate a presigned URL S3 POST request to upload a file

    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )
    try:
        response = s3_client.generate_presigned_url(
            'put_object',
            {
                'Bucket': bucket_name,
                'Key': object_name,
                'ACL': 'public-read',
                'ContentType': object_type
            },
            ExpiresIn=expiration,
        )

    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return {
        "signedRequest": response,
        'url': f'https://{bucket_name}.s3.{settings.AWS_REGION_NAME}.amazonaws.com/{object_name}'
    }


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['success'] = False
        response.data['message'] = response.data.pop('detail')
        response.data['data'] = []

    return response
