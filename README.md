The **pygbm** is a Python package designed to simulate Geometric Brownian Motions

## Features

- Base `GBMSimulator` class with core attributes and methods

## Usage

Here's a quick example of how to use the package:

```python
from pygbm.gbm_simulator import GBMSimulator
# Initialize simulator
simulator = GBMSimulator (y0 , mu , sigma )
# Simulate path
t_values , y_values = simulator . simulate_path (T, N)

