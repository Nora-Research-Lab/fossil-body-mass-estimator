![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Fossil Body Mass Estimator
 
*For paleontologists and fossil preparators: enter a single skeletal measurement and taxonomic group to instantly estimate an animal's body mass using published allometric equations.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Paleontology
 
This tool estimates the body mass of a fossil animal from a single skeletal measurement using allometric scaling equations. The user provides: (1) a measurement type selected from a dropdown (Femur Circumference, Femur Length, Humerus Circumference, or Skull Length); (2) the measurement value in centimeters as a number input; and (3) a taxonomic group from a dropdown (Theropoda, Sauropoda, Ornithopoda, Ceratopsia, Thyreophora, other non-avian dinosaur, or Mammalia). The core logic uses published regression coefficients (e.g., from Campione & Evans 2012, Campione et al. 2014, and Anderson et al. 1985) stored in a lookup table: for each combination of measurement type and taxonomic group, the tool retrieves the intercept (a) and slope (b) for the equation log10(bodymass_kg) = a + b * log10(measurement_cm). It computes the mass estimate, then also calculates the 95% confidence interval using the standard error of the estimate for that equation. The Gradio UI presents: a dropdown for measurement type, a number box for measurement (with unit label 'cm'), a dropdown for taxonomic group, and a 'Calculate' button. The output area shows the estimated body mass in kilograms (rounded to the nearest 0.1 kg) along with the 95% confidence interval in parentheses. Below that, a text line classifies the mass into one of five bins: Very small (<10 kg), Small (10–100 kg), Medium (100–1000 kg), Large (1000–10,000 kg), or Very large (>10,000 kg). No AI/ML component is used; all logic is deterministic lookups and arithmetic. The tool runs entirely client-side in Gradio with no external API calls.
 
## Run it
 
```bash
docker build -t fossil-body-mass-estimator .
docker run -p 7860:7860 fossil-body-mass-estimator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-22.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
