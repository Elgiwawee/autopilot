import boto3

def assume_role(role_arn, external_id):
    sts = boto3.client("sts")

    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="ZuhsynAutopilotSession",
        ExternalId=external_id
    )

    credentials = response["Credentials"]

    return boto3.client(
        "ec2",
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )
