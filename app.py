import gradio as gr
from fossil_body_mass_estimator import estimate_body_mass

def calculate_mass(measurement_type, measurement_value, taxonomic_group):
    if measurement_value is None or measurement_value <= 0:
        return "Error: Please enter a positive measurement value.", ""
    
    try:
        result = estimate_body_mass(measurement_type, measurement_value, taxonomic_group)
        if result["error"]:
            return f"Error: {result['error']}", ""
        
        mass_estimate = result["mass_estimate"]
        ci_lower = result["ci_lower"]
        ci_upper = result["ci_upper"]
        classification = result["classification"]
        
        mass_text = f"{mass_estimate:.1f} kg (95% CI: {ci_lower:.1f} - {ci_upper:.1f} kg)"
        classification_text = f"Classification: {classification}"
        
        return mass_text, classification_text
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}", ""

measurement_types = [
    "Femur Circumference",
    "Femur Length", 
    "Humerus Circumference",
    "Skull Length"
]

taxonomic_groups = [
    "Theropoda",
    "Sauropoda", 
    "Ornithopoda",
    "Ceratopsia",
    "Thyreophora",
    "other non-avian dinosaur",
    "Mammalia"
]

with gr.Blocks(title="Fossil Body Mass Estimator") as demo:
    gr.Markdown("# Fossil Body Mass Estimator")
    gr.Markdown("Estimate the body mass of a fossil animal based on skeletal measurements using allometric scaling equations.")
    
    with gr.Row():
        measurement_type_input = gr.Dropdown(
            choices=measurement_types,
            label="Measurement Type",
            value=measurement_types[0]
        )
        measurement_value_input = gr.Number(
            label="Measurement Value (cm)",
            value=10.0
        )
        taxonomic_group_input = gr.Dropdown(
            choices=taxonomic_groups,
            label="Taxonomic Group",
            value=taxonomic_groups[0]
        )
    
    calculate_btn = gr.Button("Calculate")
    
    with gr.Column():
        mass_output = gr.Textbox(label="Estimated Body Mass", interactive=False)
        classification_output = gr.Textbox(label="Mass Classification", interactive=False)

    calculate_btn.click(
        fn=calculate_mass,
        inputs=[measurement_type_input, measurement_value_input, taxonomic_group_input],
        outputs=[mass_output, classification_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
