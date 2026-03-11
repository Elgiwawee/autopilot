
def slo_violated(resource):
    slos = resource.serviceslo_set.all()
    for slo in slos:
        current = get_current_metric(resource, slo.metric_name)
        if current > slo.max_value:
            return True
    return False
