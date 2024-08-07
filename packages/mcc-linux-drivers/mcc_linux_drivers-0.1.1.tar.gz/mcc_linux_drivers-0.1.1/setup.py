from setuptools import setup, find_packages

setup(
    name="mcc_linux_drivers", 
    version="0.1.1",  
    author='W. Jasper',
    author_email="wjasper@ncsu.edu",
    description='Linux Drivers for MCC',
    url='https://github.com/wjasper/Linux_Drivers', 
    packages=find_packages(where='Python'),
    package_dir={'': 'Python'},
    python_requires='>=3.6',
)
