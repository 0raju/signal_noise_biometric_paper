"""
This code is part of research paper:
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

import requests
import shutil
from pathlib import Path
from zipfile import ZipFile
from tqdm.auto import tqdm
import os
import tempfile

def download_zip(URL, zip_dir):
    """
    Download a zip file from the given URL, if not already downloaded.
    """
    zip_path = Path(zip_dir) / Path(URL).name
    if zip_path.exists():
        print(f"{zip_path.name} already exists. Skipping download.")
        return zip_path
    print(f"Downloading {zip_path.name}...")
    with requests.get(URL, stream=True, allow_redirects=True) as r:
        r.raise_for_status()  # Check for request errors
        file_size = int(r.headers.get("Content-Length", 0))
        with tqdm.wrapattr(r.raw, "read", total=file_size, desc=f"Downloading {zip_path.name}") as raw:
            with open(zip_path, "wb") as f:
                shutil.copyfileobj(raw, f)
    return zip_path

def extract_and_flatten(zip_path, flatten_dir):
    """
    Extract nested zip files into a temporary directory and then flatten the structure, with progress tracking.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Using temporary directory: {temp_dir}")
        # Extract the initial zip file
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        # Recursively extract any found zip files
        extract_nested_zips(Path(temp_dir))
        # Flatten the directory structure
        flatten_directory(Path(temp_dir), Path(flatten_dir))
        print(f"All files have been processed and moved to: {flatten_dir}")

def extract_nested_zips(base_path):
    """
    Recursively find and extract all zip files in the directory, with progress tracking.
    """
    zip_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(base_path) for f in filenames if f.endswith('.zip')]
    for zip_file in tqdm(zip_files, desc='Extracting nested ZIPs'):
        with ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(Path(zip_file).parent)
        os.remove(zip_file)

def flatten_directory(source_directory, target_directory):
    """
    Move all files from nested directories to a single flat directory, with progress tracking.
    """
    target_directory.mkdir(parents=True, exist_ok=True)
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(source_directory) for f in filenames]
    for file in tqdm(files, desc='Flattening directory'):
        src_file_path = Path(file)
        dst_file_path = target_directory / src_file_path.name
        counter = 1
        while dst_file_path.exists():
            dst_file_path = target_directory / f"{dst_file_path.stem}_{counter}{dst_file_path.suffix}"
            counter += 1
        shutil.move(src_file_path, dst_file_path)


if __name__ == "__main__":

    URL = 'https://figshare.com/ndownloader/files/27039812'
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zip_dir = os.path.join(base_dir, 'data', 'zip')
    flatten_dir = os.path.join(base_dir, 'data', 'gazebase_v2', 'raw')
    
    os.makedirs(zip_dir, exist_ok=True)

    # Step 1: Download the zip file
    zip_path = download_zip(URL, zip_dir)

    # Step 2 & 3: Extract nested zips and flatten the directory structure
    extract_and_flatten(zip_path, flatten_dir)

    print("Process completed successfully.")
