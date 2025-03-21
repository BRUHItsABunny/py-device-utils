from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "betterproto @ git+https://github.com/ii64/python-betterproto.git#egg=betterproto",
    "grpclib~=0.4.7",
    "pydantic>=1.8.0,<2",
    "aiohttp>=3.9.4",
]

setup(
    name="deviceutils",
    version="1.0.6",
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