def energy_suggestion(energy_usage):
    if energy_usage > 10:
        return "Consider using energy-efficient appliances."
    return "Energy usage is within acceptable limits."

def waste_suggestion(waste_generation):
    if waste_generation > 100:
        return "Increase recycling efforts."
    return "Waste generation is within acceptable limits."

def travel_suggestion(business_travel):
    if business_travel > 5:
        return "Consider video conferencing instead of travel."
    return "Business travel is within acceptable limits."
