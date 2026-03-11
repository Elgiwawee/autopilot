from actions.base import CloudAction


class StopEC2Instance(CloudAction):

    def __init__(self, instance_id, region):
        self.instance_id = instance_id
        self.region = region

    def execute(self, session):
        ec2 = session.client("ec2", region_name=self.region)
        ec2.stop_instances(InstanceIds=[self.instance_id])

    def rollback(self, session):
        ec2 = session.client("ec2", region_name=self.region)
        ec2.start_instances(InstanceIds=[self.instance_id])
