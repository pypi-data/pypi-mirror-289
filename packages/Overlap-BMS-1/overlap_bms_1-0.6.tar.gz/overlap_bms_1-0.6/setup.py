
# setup.py
from setuptools import setup, find_packages

setup(
    name='Overlap_BMS_1',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'ipywidgets',
        'IPython',
    ],
    include_package_data=True,
    description='A library for interactive data analysis with widgets.',
)
