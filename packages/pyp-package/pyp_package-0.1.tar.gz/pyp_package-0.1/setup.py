from setuptools import setup,find_packages

setup(
  name='pyp_package',
  version='0.1',
  packages=find_packages(),
  install_requires=[
    'numpy>=1.1.1'
  ]
)