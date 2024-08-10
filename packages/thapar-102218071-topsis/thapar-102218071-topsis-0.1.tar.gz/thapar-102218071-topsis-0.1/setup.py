import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
setup(
    name='thapar-102218071-topsis',
    version='0.1',
    author='Sanchit2004',
    author_email='sanchitm990@gmail.com',
    description='A Python package for implementing the TOPSIS method',
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis=my_topsis_package.__main__:topsis',  # Ensure this matches the file name
        ],
    },
    install_requires=[
        'pandas',
        'numpy',
    ],
)