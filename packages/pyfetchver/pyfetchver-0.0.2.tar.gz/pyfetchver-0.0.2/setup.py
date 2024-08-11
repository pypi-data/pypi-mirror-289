from setuptools import *
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name="pyfetchver",
  version="0.0.2",
  description="Simple python test",
  author="Anh_111",
  packages=find_packages(),
  long_description=long_description,
  long_description_content_type='text/markdown',
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=[
        'GPUtil',
        'psutil',
        'colorama'
  ],
  python_requires=">=3.6",
)