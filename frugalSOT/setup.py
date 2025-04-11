from setuptools import setup, find_packages

setup(
    name="frugalsot",
    version="1.0.0",
    packages=find_packages(),
    scripts=['bin/frugalsot'],
    
    # Dependencies
    install_requires=[
        "nltk==3.9.1",
        "scikit-learn==1.5.1", 
        "sentence-transformers==3.3.1",
        "python-dotenv==1.0.1",
        "setuptools==59.6.0"
    ],

    # Package metadata
    author="FrugalSOT Team",
    author_email="frugalsot@gmail.com",
    description="Optimized AI Inference for Edge Devices",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HARISH20205/RPI",
    
    # Include non-Python files
    package_data={
        "frugalsot": [
            "scripts/*.sh",
            "data/*.json"
        ]
    },
    include_package_data=True,
    
    # PyPI classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
)