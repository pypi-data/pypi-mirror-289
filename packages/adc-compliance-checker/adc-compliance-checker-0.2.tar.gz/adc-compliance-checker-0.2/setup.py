from setuptools import setup, find_packages

setup(
    name='adc-compliance-checker',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # List package dependencies
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
