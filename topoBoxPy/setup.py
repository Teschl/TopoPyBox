from setuptools import setup, find_packages

setup(
    name='topoBoxPy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            # If your package includes any command-line scripts, define them here
        ],
    },
    author=['Wolfgang Schwanghart', 'Theophil Bringezu'],
    author_email=['schwangh@uni-potsdam.de','bringezu1@uni-potsdam.de'],
    description="The Python version of the TopoToolBox for MATLAB",
)
