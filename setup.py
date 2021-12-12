from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='jtils',
    version='0.1',
    description='General utilities.',
    author='James Thornton',
    author_email='jamestomthornton@gmail.com',
    url='https://github.com/JTT94/jtils',
    packages=find_packages(),
    install_requires=requirements,
)