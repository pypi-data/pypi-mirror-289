import pathlib
from setuptools import setup,find_packages # type: ignore

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102218026-topsiss",
    version="1.0.0",
    description="ranking according to your prefrence",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Shubhamaggarwal6/calculate_performance_scores",
    author="shubham",
    author_email="09shubhamaggarwal@gmial.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
        packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            '102218026-topsiss=topsiss_102218026.__main__:main',
        ],
    },
)