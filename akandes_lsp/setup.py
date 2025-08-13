from setuptools import setup, find_packages

setup(
    name="akandes-language",
    version="0.1.0",
    description="Akandes Language: Modular, agentic EDA/HDL/AI platform",
    author="Akande Joseph",
    author_email="manager@continentalrock.net",
    packages=find_packages(),
    install_requires=[
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "akandes-chips=chips:main"
        ]
    },
    python_requires=">=3.8",
    include_package_data=True,
    url="https://github.com/Admire2/akandes-language",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
