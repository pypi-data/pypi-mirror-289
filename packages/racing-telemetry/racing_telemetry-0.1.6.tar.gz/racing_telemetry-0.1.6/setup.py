from setuptools import find_packages, setup

setup(
    name="racing-telemetry",
    version="0.1.6",
    packages=find_packages(include=["racing_telemetry", "racing_telemetry.*"]),
    install_requires=[
        "gql",
        "requests",
        "influxdb-client",
        "pandas",
        "requests-toolbelt",
        "psycopg2-binary",
        "sqlalchemy",
    ],
    author="Marcel Hild",
    author_email="hild@b4mad.net",
    description="A library for telemetry data analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/b4mad/racing-telemetry",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
