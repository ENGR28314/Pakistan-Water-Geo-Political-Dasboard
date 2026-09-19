def run_scenario(flow_change, storage_percent, demand_percent):
    """
    Transparent educational indicator.
    It is not a calibrated hydraulic model and must not be used for operational allocation.
    """
    flow_index = max(0.0, 100.0 + float(flow_change))
    storage_index = max(0.0, min(100.0, float(storage_percent)))
    demand_index = max(0.0, float(demand_percent))
    supply_index = 0.65 * flow_index + 0.35 * storage_index
    stress = max(0.0, demand_index - supply_index)
    if stress < 10:
        label = "Low"
    elif stress < 25:
        label = "Moderate"
    else:
        label = "High"
    return {
        "flow_index": flow_index,
        "storage_index": storage_index,
        "demand_index": demand_index,
        "supply_index": supply_index,
        "stress": stress,
        "stress_label": label,
    }
