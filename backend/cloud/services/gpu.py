
# monitoring/services/gpu.py

def list_gpus(organization, cloud=None):
    """
    Returns GPU inventory per cloud.
    This is stubbed now, real scanners come later.
    """

    inventory = []

    if cloud in (None, "aws"):
        inventory.append({
            "cloud": "aws",
            "total_gpus": get_gpu_count(organization, "aws"),
            "regions": [
                {
                    "region": "us-east-1",
                    "gpus": 4,
                    "instance_types": ["g4dn.xlarge", "p3.2xlarge"],
                },
                {
                    "region": "eu-west-1",
                    "gpus": 4,
                    "instance_types": ["g5.xlarge"],
                },
            ],
        })

    return inventory


def get_gpu_count(organization, cloud=None, region=None):
    """
    Simple aggregate count.
    """
    return 8

