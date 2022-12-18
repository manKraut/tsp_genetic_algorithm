from setuptools import setup, find_packages
setup(
    name="tsp",
    python_requires=">=3.6.8",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib"
    ],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "tsp=tsp.main:main",
        ],
    },
)