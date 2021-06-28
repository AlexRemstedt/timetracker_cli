from importlib.metadata import entry_points
from setuptools import setup, find_packages


def _read_requirements():
    with open('requirements.txt') as req:
        content = req.readlines()
    return content


setup(
    name='tt',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=_read_requirements(),
    entry_points="""
        [console_scripts]
        tt=tt.cli:cli
    """
)
