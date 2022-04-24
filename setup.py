# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import setuptools

from customplotlib import __version__

setuptools.setup(
    name='customplotlib',
    version=__version__,
    description='customplotlib',
    author='Joe Day',
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'seaborn',
    ],
    packages=setuptools.find_packages(include='customplotlib.*'),
    zip_safe=False
)
