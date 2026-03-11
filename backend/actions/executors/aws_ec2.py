import boto3
from django.utils.timezone import now


def stop_ec2_instance(resource, credentials):
    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

    ec2.stop_instances(InstanceIds=[resource.external_id])
