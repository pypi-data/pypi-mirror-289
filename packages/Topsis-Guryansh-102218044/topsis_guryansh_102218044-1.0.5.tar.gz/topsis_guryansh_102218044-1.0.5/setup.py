import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="Topsis-Guryansh-102218044",
    version="1.0.5",
    description="Python package for Topsis Analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Guryansh/topsis",
    author="Guryansh",
    author_email="guryanshsingla@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["guryansh_topsis"],
    include_package_data=True,
    install_requires=['argparse', 'pandas', 'numpy'],
    entry_points={"console_scripts": ["guryansh_topsis=guryansh_topsis.__main__:main"]},
)
