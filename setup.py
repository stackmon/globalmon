from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name='globalmon',  # Name of the package
    version='0.1.0',  # Version number
    description='Global URL monitoring',
    long_description=open('README.md').read(),  # Description from README file
    long_description_content_type='text/markdown',
    url='https://github.com/stackmon/globalmon',  # URL to your package's repository
    author='Muneeb H. Jan',
    author_email='muneeb-hafeez.jan@t-systems.com',
    license='Apache License Version 2.0',  # License type

    # Keywords to indicate what your project is about
    keywords='global URL monitoring endpoints',

    test_suite='tests',  # Tells setuptools where to find the tests
    tests_require=[
        #'unittest',
        'requests-mock',
    ],  # Specify any test dependencies here
    
    # Packages to include
    package_dir={'':'src'},
    packages=[
        'globalmon',
    ],

    #Dependencies
    install_requires=[
        'PyYAML',
        'requests',
        'statsd',
        # Add more dependencies as needed
    ],

    # Entry points
    entry_points={
        'console_scripts': [
            'globalmon = globalmon.server:main',  # Example command-line script
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
