from setuptools import setup, find_packages
import os


def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


setup(
    name="security-toolkit",
    version="0.2",
    author="Jonathen Cuvelier",
    description="A collection of tools for security analysis",
    packages=find_packages(),
    install_requires=parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),
    entry_points={
        'console_scripts': [
            'security-toolkit=toolkit.main:main',  # Replace with your CLI entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
