from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dfuss",
    version="0.0.0",
    description="D-FUSS: Discrete-FoUrier SerieS",
    long_description=long_description,
    long_description_content_type="text/markdown",
        
    author="aletgn",
    author_email="-",
    url="https://github.com/aletgn/d-fuss.git",
    project_urls = {"Bug Tracker": "https://github.com/aletgn/d-fuss/issues"},
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy", "scipy", "matplotlib"],
    extras_require={"test" : ["notebook"],
                    "dev" : ["pytest", "twine", "setuptools", "build"]}
)