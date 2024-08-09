import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mumuai", # Replace with your own username
    version="0.1.0",
    author="Mumu Hong",
    author_email="mumuai@goatfarm.ai",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dltdnfrk/psh",
    license='MIT',
    packages=setuptools.find_packages(include=['mumuai', 'mumuai.*']),
    keywords=['mumuai'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Scheduling",
    ],
    python_requires='>=3.6',
)