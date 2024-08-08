from setuptools import setup, find_packages

setup(
    name="mlvpn",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "mlvpn=cli.cli:cli",
        ],
    },
)
