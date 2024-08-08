from setuptools import setup, find_packages

setup(
    name='nonstdout',
    version='1.0.0',
    author='Sushii64',
    packages=find_packages(),
    description='A Python library for making printing cooler with colours and loading bars.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sushii64/nonstdout',
    license='GNU GPL V3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
