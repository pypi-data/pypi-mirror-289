import setuptools
import os
import re


def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'adc_compliance_checker', '__init__.py')
    with open(version_file, 'r') as f:
        version_content = f.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_content, re.MULTILINE)
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='adc-compliance-checker',
    version=read_version(),  # Use the version from __init__.py
    packages=setuptools.find_packages(),
    install_requires=[
        'xarray',
        'pathlib',
        'netCDF4',
        'h5netcdf'
    ],
    author='Alessio Canclini',
    author_email='alessioc@met.no',
    description='ADC Compliance Checker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Alessimc/adc-compliance-checker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'adc-compliance-checker=adc_compliance_checker.cli:main',
        ],
    },
    license='GPLv3',
)
