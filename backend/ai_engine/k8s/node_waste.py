# ai_engine/k8s/node_waste.py
def calculate_waste(cpu_used, cpu_total, mem_used, mem_total):
    cpu_eff = cpu_used / cpu_total
    mem_eff = mem_used / mem_total

    efficiency = min(cpu_eff, mem_eff)
    waste = 1 - efficiency

    return round(waste * 100, 2)
