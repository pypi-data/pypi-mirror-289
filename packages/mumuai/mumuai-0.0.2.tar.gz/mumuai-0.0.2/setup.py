import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mumuai", # Replace with your own username
    version="0.0.2",
    author="Example Author",
    author_email="mumuai@goatfarm.ai",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dltdnfrk/psh",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    keywords=['pyxing'],
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)