from setuptools import setup, find_packages

with open("pyproject.toml", encoding="utf-8") as f:
    pyproject_data = f.read()

setup(
    name="pymft",
    version="0.1.2",
    description="Library for Midi Fighter Twister Interfacing in Python",
    author="Sina Solaimanpour",
    author_email="sinas.cb@gmail.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["python-rtmidi>=1.5.8", "typing>=3.7.4"],
    entry_points={
        "console_scripts": [
            "demo_main=pymft.main:run",
            "version=pymft.main:version",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)