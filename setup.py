# setup.py
from setuptools import find_packages, setup

setup(
    name="iCompress",  # Replace 'your_package_name' with the name of your package
    version="0.1.0",  # The version of your package
    description="A simple compression hub",  # A short description of your package
    long_description=open(
        "README.md"
    ).read(),  # Long description read from the README.md file
    long_description_content_type="text/markdown",  # Type of the long description content
    author="Your Name",  # Your name or your organization's name
    author_email="your_email@example.com",  # Your email or your organization's email
    url="https://github.com/yourusername/your_package_name",  # URL to the project homepage or repository
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        "pydub",
        "Pillow",
        "ffmpeg-python",
        # List of dependencies as strings, e.g., 'numpy >= 1.14.5'
    ],
    classifiers=[
        # Trove classifiers
        # Full list at https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum version requirement of the Python for your package
    include_package_data=True,  # Include everything in source control
    zip_safe=False,  # Do not package the project as an .egg file
)
