from pathlib import Path

from setuptools import find_packages, setup


with open(
    Path(__file__).parent.resolve() / "cloudwatch" / "VERSION", encoding="utf-8"
) as ver:
    version = ver.readline().rstrip()


with open("requirements.txt", encoding="utf-8") as req:
    requirements = [r.rstrip() for r in req.readlines()]



setup(
    name="cloudwatcher",
    version=version,
    author="Markus Scharitzer",
    author_email="markus@scharitzer.io",
    description="Cloud Vulnerability Watch Platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/droptableuser/cloudwatch",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={},
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={"web_environment": ["cloudwatch=cloudwatch.app:app"]},
    python_requires=">=3.8.5",
)