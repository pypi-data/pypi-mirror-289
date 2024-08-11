from setuptools import setup, find_packages

setup(
    name="prompteval",  # Replace with your desired package name
    version="0.0.1",
    packages=find_packages(),
    description="prompt evaluation toolkit",
    long_description="prompt evaluation toolkit for testing and evaluating prompts",
    long_description_content_type="text/markdown",
    author="Esco Obong",
    author_email="esco@hbyte.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

