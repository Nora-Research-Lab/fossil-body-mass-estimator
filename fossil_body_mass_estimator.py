import math

# Allometric scaling coefficients from literature
# Format: (intercept, slope, std_error)
# Sources: Campione & Evans 2012, Campione et al. 2014, Anderson et al. 1985
COEFFICIENTS = {
    ("Femur Circumference", "Theropoda"): (-2.490, 2.730, 0.280),
    ("Femur Circumference", "Sauropoda"): (-2.050, 2.350, 0.210),
    ("Femur Circumference", "Ornithopoda"): (-2.340, 2.710, 0.270),
    ("Femur Circumference", "Ceratopsia"): (-2.170, 2.550, 0.240),
    ("Femur Circumference", "Thyreophora"): (-2.510, 2.750, 0.290),
    ("Femur Circumference", "other non-avian dinosaur"): (-2.490, 2.730, 0.280),
    ("Femur Circumference", "Mammalia"): (-2.060, 2.450, 0.220),
    
    ("Femur Length", "Theropoda"): (-2.720, 2.860, 0.310),
    ("Femur Length", "Sauropoda"): (-2.290, 2.480, 0.230),
    ("Femur Length", "Ornithopoda"): (-2.570, 2.840, 0.300),
    ("Femur Length", "Ceratopsia"): (-2.400, 2.680, 0.260),
    ("Femur Length", "Thyreophora"): (-2.740, 2.880, 0.320),
    ("Femur Length", "other non-avian dinosaur"): (-2.720, 2.860, 0.310),
    ("Femur Length", "Mammalia"): (-2.300, 2.630, 0.240),
    
    ("Humerus Circumference", "Theropoda"): (-2.450, 2.680, 0.270),
    ("Humerus Circumference", "Sauropoda"): (-2.010, 2.300, 0.200),
    ("Humerus Circumference", "Ornithopoda"): (-2.300, 2.660, 0.260),
    ("Humerus Circumference", "Ceratopsia"): (-2.130, 2.500, 0.230),
    ("Humerus Circumference", "Thyreophora"): (-2.470, 2.700, 0.280),
    ("Humerus Circumference", "other non-avian dinosaur"): (-2.450, 2.680, 0.270),
    ("Humerus Circumference", "Mammalia"): (-2.020, 2.400, 0.210),
    
    ("Skull Length", "Theropoda"): (-2.610, 2.770, 0.300),
    ("Skull Length", "Sauropoda"): (-2.180, 2.400, 0.220),
    ("Skull Length", "Ornithopoda"): (-2.460, 2.750, 0.290),
    ("Skull Length", "Ceratopsia"): (-2.290, 2.590, 0.250),
    ("Skull Length", "Thyreophora"): (-2.630, 2.790, 0.310),
    ("Skull Length", "other non-avian dinosaur"): (-2.610, 2.770, 0.300),
    ("Skull Length", "Mammalia"): (-2.150, 2.520, 0.230),
}

def estimate_body_mass(measurement_type, measurement_value, taxonomic_group):
    """
    Estimate body mass using allometric scaling equations.
    
    Args:
        measurement_type (str): Type of measurement (e.g., "Femur Circumference")
        measurement_value (float): Measurement in cm
        taxonomic_group (str): Taxonomic group
        
    Returns:
        dict: Contains mass_estimate, ci_lower, ci_upper, classification, and error
    """
    # Validate inputs
    if measurement_value <= 0:
        return {"error": "Measurement value must be positive", "mass_estimate": 0, "ci_lower": 0, "ci_upper": 0, "classification": ""}
    
    key = (measurement_type, taxonomic_group)
    if key not in COEFFICIENTS:
        return {"error": f"No coefficient data available for {measurement_type} in {taxonomic_group}", "mass_estimate": 0, "ci_lower": 0, "ci_upper": 0, "classification": ""}
    
    # Get coefficients
    a, b, se = COEFFICIENTS[key]
    
    # Calculate log10(mass) using the allometric equation
    log_measurement = math.log10(measurement_value)
    log_mass = a + b * log_measurement
    
    # Convert back to mass in kg
    mass_estimate = 10 ** log_mass
    
    # Calculate 95% confidence interval
    # Using z-score of 1.96 for 95% CI
    z_score = 1.96
    log_ci_lower = log_mass - z_score * se
    log_ci_upper = log_mass + z_score * se
    
    ci_lower = 10 ** log_ci_lower
    ci_upper = 10 ** log_ci_upper
    
    # Classify mass
    classification = classify_mass(mass_estimate)
    
    return {
        "mass_estimate": mass_estimate,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "classification": classification,
        "error": ""
    }

def classify_mass(mass_kg):
    """
    Classify the mass into size categories.
    
    Args:
        mass_kg (float): Body mass in kg
        
    Returns:
        str: Size category
    """
    if mass_kg < 10:
        return "Very small (<10 kg)"
    elif mass_kg < 100:
        return "Small (10–100 kg)"
    elif mass_kg < 1000:
        return "Medium (100–1000 kg)"
    elif mass_kg < 10000:
        return "Large (1000–10,000 kg)"
    else:
        return "Very large (>10,000 kg)"
