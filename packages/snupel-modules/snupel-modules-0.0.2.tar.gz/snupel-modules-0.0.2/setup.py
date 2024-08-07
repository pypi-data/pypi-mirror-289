import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snupel-modules", # Replace with your own username
    version="0.0.2",
    author="WonSeok Choi",
    author_email="wschoi0312@snu.ac.kr",
    description="Seoul National University Production Engineering Laboratory Machine Learning Simulation Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)