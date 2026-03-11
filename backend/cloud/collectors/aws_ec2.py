import boto3
from cloud.models import CloudAccount, CloudResource, CloudProvider
from cloud.cost.ec2_cost import calculate_ec2_hourly_cost


def collect_ec2_instances(cloud_account_id):
    cloud_account = CloudAccount.objects.get(id=cloud_account_id)
    provider = CloudProvider.objects.get(name="aws")

    # Assume role
    session = boto3.Session()
    sts = session.client("sts")

    assumed = sts.assume_role(
        RoleArn=cloud_account.role_arn,
        RoleSessionName="cloud-autopilot-session",
    )

    credentials = assumed["Credentials"]

    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
        region_name=cloud_account.region,  # recommended if stored
    )

    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):

                # 🔹 Calculate cost
                hourly_cost = calculate_ec2_hourly_cost(instance)

                CloudResource.objects.update_or_create(
                    cloud_account=cloud_account,
                    external_id=instance["InstanceId"],
                    defaults={
                        "provider": provider,
                        "resource_type": "vm",
                        "region": ec2.meta.region_name,
                        "state": instance["State"]["Name"],
                        "cost_per_hour": hourly_cost,
                        "metadata": instance,
                    },
                )
