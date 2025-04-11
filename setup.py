from setuptools import setup, find_packages

setup(
    name="dpj",  # Name of the package
    version="3.0.0",  # Version of the package
    description="A CLI Encryption Application",
    long_description=open('README.md').read(),  # README file for project description
    long_description_content_type="text/markdown",  # Format of the README
    author="Jheff MAT",  # Author information
    author_email="Jheff.at@gmail.com",  # Author's email
    url="https://github.com/jheffat/-DPJ",  # URL to the project
    packages=find_packages(),  # Automatically find packages (dpj, tests, etc.)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",  # Adjust to the Python versions you support
    ],
    install_requires=[ "cryptography>=3.0",  "argparse>=1.4", ,"bcrypt>=4.1.2" ,"keyboard>=0.13.5"    
    ],
    entry_points={  # CLI command entry points
        'console_scripts': [
            'dpj=dpj.dpj:main',  # This maps the dpj command to the main function in dpj.py
        ],
    },
    python_requires='>=3.6',  # Specify Python version compatibility
)