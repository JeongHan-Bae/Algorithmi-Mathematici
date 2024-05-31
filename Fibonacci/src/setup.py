import os
import shutil
import numpy as np
from setuptools import setup
from Cython.Build import cythonize

# Build the Cython extension
setup(
    ext_modules=cythonize("fibonacci.pyx"),
    include_dirs=[np.get_include()]
)

# Remove the build directory
shutil.rmtree('build', ignore_errors=True)

# Copy the built .pyd file to the ../target/ directory
for file in os.listdir():
    if file.endswith(".pyd"):
        shutil.copy(file, os.path.join("..", "target", file))
