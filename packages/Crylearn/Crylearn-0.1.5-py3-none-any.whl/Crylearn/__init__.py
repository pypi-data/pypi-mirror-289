"""
Crylearn Package

This package provides tools for processing crystal structure data and converting them into graph representations.
"""
import importlib.util
import sys
import os

# Determine the base path of the Crylearn package
base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the path of the compiled module
compiled_module_path = os.path.join(base_path, '__pycache__', 'cry2graph.cpython-39.pyc')

# Check if the compiled module exists
if not os.path.exists(compiled_module_path):
    raise FileNotFoundError(f"The compiled module '{compiled_module_path}' was not found.")

# Load the module
spec = importlib.util.spec_from_file_location("Crylearn.cry2graph", compiled_module_path)
cry2graph = importlib.util.module_from_spec(spec)
sys.modules["Crylearn.cry2graph"] = cry2graph
spec.loader.exec_module(cry2graph)
