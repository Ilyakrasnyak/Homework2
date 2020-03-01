from setuptools import setup, find_packages
from os.path import join, dirname
import external_sort

setup(
    name='external_sort',
    version=external_sort.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['external_sort = external_sort.start:star']
    }
)