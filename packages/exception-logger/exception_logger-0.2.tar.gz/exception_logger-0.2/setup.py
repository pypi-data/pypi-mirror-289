from setuptools import setup, find_packages

setup(
    name='exception-logger',
    version='0.2',  # Update this to a new version number
    packages=find_packages(),
    install_requires=[
        'Flask',
        'mysql-connector-python',
        # other dependencies
    ],
    # other metadata
)
