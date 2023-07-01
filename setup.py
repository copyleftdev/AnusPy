from setuptools import setup, find_packages

setup(
    name='AnusPy',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='AnusPy is a Python package for translating clinch codes into alphanumeric characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['numpy'],  # Add your project dependencies here
    url='https://github.com/copyleftdev/AnusPy',
    author='Copyleftdev',
    author_email='dj@codetestcode.io'
)