# cloud/services/ec2_discovery.py

def list_ec2_instances(ec2_client):
    response = ec2_client.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "instance_id": instance["InstanceId"],
                "instance_type": instance["InstanceType"],
                "state": instance["State"]["Name"],
                "availability_zone": instance["Placement"]["AvailabilityZone"],
            })

    return instances


