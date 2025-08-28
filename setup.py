from setuptools import setup, find_packages

setup(
    name="network-packet-analyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "colorama>=0.4.6",
        "scapy>=2.5.0",
    ],
    entry_points={
        "console_scripts": [
            "npa=npa.cli:main",
        ],
    },
    author="Zee",
    author_email="your.email@example.com",
    description="A professional-grade network packet analyzer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/NetworkPacketAnalyzer",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
) 