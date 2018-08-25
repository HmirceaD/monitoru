"""setup file for installing and distributing monitoru project"""

from setuptools import setup
from setuptools import find_packages

setup(name='monitoru',
      version='0.1',
      description="Client side monitoring system for your pc's metrics",
      url='https://github.com/HmirceaD/monitoru.git',
      author='Mircea Dan',
      install_requires=['pika', 'psutil', 'flask'],
      author_email='mircea_dan97@yahoo.com',
      entry_points={
        'console_scripts': [
            'monitoru_client = client.main_loop:init_client',
            'monitoru_server = server.app:start_server',

        ]},
      packages=find_packages())
