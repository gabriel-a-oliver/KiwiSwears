from setuptools import setup, find_packages

setup(name='kiwi-swears',
      version='0.0.1',
      description='A discord bot to manage your swear jar',
      url='https://github.com/bpas247/KiwiSwears',
      author='Brady Pascoe, Gabriel Oliver',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'discord.py',
      ])
