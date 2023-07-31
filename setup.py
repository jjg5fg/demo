
from setuptools import setup, find_packages



setup(

    name='demo',

    version='1.0.0',

    url='https://github.com/jjg5fg/demo.git',

    author='Author Name',

    author_email='author@gmail.com',

    description='Description of my package',

    packages=find_packages(),    

    install_requires=['pandas >=0.20'],

)
