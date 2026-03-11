# ai_engine/instance_families.py

INSTANCE_FAMILIES = {
    "t3": ["t3.nano", "t3.micro", "t3.small", "t3.medium", "t3.large", "t3.xlarge"],
    "m5": ["m5.large", "m5.xlarge", "m5.2xlarge", "m5.4xlarge"],
    "c5": ["c5.large", "c5.xlarge", "c5.2xlarge"],
}


def get_family(instance_type):
    return instance_type.split(".")[0]


def smaller_instance(instance_type):
    family = get_family(instance_type)
    sizes = INSTANCE_FAMILIES.get(family, [])

    if instance_type not in sizes:
        return None

    index = sizes.index(instance_type)
    if index == 0:
        return None  # already smallest

    return sizes[index - 1]
