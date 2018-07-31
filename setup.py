"""setup file for installing and distributing monitoru project"""

from setuptools import setup
from setuptools import find_packages

setup(name='monitoru',
      version='0.1',
      description="Client side monitoring system for your pc's metrics",
      url='https://github.com/HmirceaD/monitoru.git',
      author='Mircea Dan',
      install_requires=['pika', 'psutil'],
      author_email='mircea_dan97@yahoo.com',
      packages=find_packages())
