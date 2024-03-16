from setuptools import setup, find_packages

setup(
    name="pycx3",
    version="1.0.3",
    description="Compiler Python version 3 source file to binary",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Rangga Fajar Oktariansyah",
    author_email="fajarrkim@gmail.com",
    url="https://github.com/FajarKim/pycx3",
    python_requires=">=3.8",
    packages=find_packages(),
    keywords="python2 cython compiler performance legacy",
    install_requires=[
        "Cython>=0.29.34"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    project_urls={
        "Documentation": "https://github.com/FajarKim/pycx3#readme",
        "Donate": "https://buymeacoffee.com/fajarkim",
        "Source Code": "https://github.com/FajarKim/pycx3",
        "Bug Tracker": "https://github.com/FajarKim/pycx3/issues"
    },
    entry_points={
        "console_scripts": [
            "pycx3 = pycx3.cli:compile"
        ]
    },
    license="AGPL-3.0"
)
