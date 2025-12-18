"""Setup script for the calculator application."""

from setuptools import setup, find_packages

setup(
    name="simple-calculator",
    version="1.0.0",
    description="A simple calculator application for testing",
    author="Test User",
    author_email="test@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
