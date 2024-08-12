import re
from pathlib import Path

import pkg_resources as pkg
from setuptools import setup
from setuptools import find_packages, setup



def get_requirements():
    file = ROOT / 'requirements.txt'
    all_txt = file.read_text()
    return all_txt.split('\n')
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
#reqs = [str(ir.req) for ir in install_reqs]
# Settings
FILE = Path(__file__).resolve()
ROOT = FILE.parent  # root directory
README = (ROOT / "README.md").read_text(encoding="utf-8")
#REQUIREMENTS = [f'{x.name}{x.specifier}' for x in pkg.parse_requirements((ROOT / 'requirements.txt').read_text())]
REQUIREMENTS = get_requirements()

def get_version():
    file = ROOT / 'linguanova/__init__.py'
    return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(), re.M)[1]
setup(
    name="lingua-nova",  # name of pypi package
    version=get_version(),  # version of pypi package
    python_requires=">=3.8.0",
    long_description=README,
    long_description_content_type="text/markdown",
    project_urls={
        'Bug Reports': 'https://github.com/de-la-Vietnamita/LinguaNova/issues',
        'Source': 'https://github.com/de-la-Vietnamita/LinguaNova',},
    author="de-la-Vietnamita",
    author_email='ductq1801@gmail.com',
    #packages=['linguanova'],  # required
    packages=find_packages(),  # required
    #include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'pytest-cov', 'coverage'],},
    classifiers=[
        "Intended Audience :: Developers", "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)", "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", "Programming Language :: Python :: 3.10",
        "Topic :: Software Development", "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS", "Operating System :: Microsoft :: Windows"],
    keywords="machine-learning, deep-learning, Speech, ML, DL, AI, LinguaNova")