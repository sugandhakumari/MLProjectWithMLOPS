from setuptools import setup, find_packages

setup(
    name="mlProject",
    version="0.0.0",
    description="ML project with MLOps integration",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
