from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "betterproto>=1.2.5",
]

setup(
    name="deviceutils",
    version="1.0.0",
    author="BRUHItsABunny",
    author_email="",
    description="Android utilities all in one spot, python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/BRUHItsABunny/py-device-utils/",
    packages=find_packages(exclude=["tests", "test"]),
    package_data={"deviceutils": ["py.typed", "device_utils_pb2.pyi"]},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)