from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name='globalmon',  # Name of your package
    version='0.1.0',  # Version number
    description='Global URL monitoring',
    long_description=open('README.md').read(),  # Description from README file
    long_description_content_type='text/markdown',
    url='https://github.com/stackmon/global-mon',  # URL to your package's repository
    author='Muneeb H. Jan',
    author_email='muneeb-hafeez.jan@t-systems.com',
    license='Apache License Version 2.0',  # License type

    # Keywords to indicate what your project is about
    keywords='global URL monitoring endpoints',
    
    # Packages to include
    packages=find_packages(),

    #Dependencies
    install_requires=[
        'PyYAML',
        # Add more dependencies as needed
    ],

    # Entry points
    entry_points={
        'console_scripts': [
            'globalmon = src.server:main',  # Example command-line script
        ],
    },

    # Additional classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        # Add more classifiers as needed
    ],
)
