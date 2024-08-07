from setuptools import setup, find_packages

with open('./requirements.txt') as f:
  requirements = f.read().splitlines()
requirements = [x for x in requirements if not any([y for y in ['grpcio-tools', 'protobuf'] if y in x])]
setup(
  name='pyfutugrpc',
  version='0.1',
  packages=find_packages(),
  install_requires=requirements,
)
