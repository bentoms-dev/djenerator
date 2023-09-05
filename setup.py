from setuptools import setup, find_packages

setup(
    name='djenerator',
    version='0.1',
    packages=find_packages(),
    install_requires=['mido'],  # Add any dependencies here
    entry_points={
        'console_scripts': [
            'djenerator = djenerator.generate:main'
        ],
    },
)
