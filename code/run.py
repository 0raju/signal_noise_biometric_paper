"""
This code is part of research paper
Title: Signal vs Noise in Eye-tracking Data: Biometric Implications and Identity Information Across Frequencies.
Authors: Mehedi Hasan Raju, Lee Friedman, Dillon Lohr, and Oleg V. Komogortsev.
Published: 2024 Symposium on Eye Tracking Research and Applications (ETRA '24).
DOI: https://doi.org/10.1145/3649902.3653353

This work and its accompanying codebase are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License 
(https://creativecommons.org/licenses/by-nc-sa/4.0/). 

For all other uses, please contact the Office for Commercialization and Industry Relations at Texas State University http://www.txstate.edu/ocir/

Property of Texas State University.

For inquiries and further information, please contact Mehedi Hasan Raju (m.raju@txstate.edu)

"""

import subprocess

script_paths = [
        'url_to_csv.py', 
        'data_processing.py', 
        'signal_noise_separation.py'
    ]

for script in script_paths:

    result = subprocess.run(['python', script], capture_output=True, text=True)


