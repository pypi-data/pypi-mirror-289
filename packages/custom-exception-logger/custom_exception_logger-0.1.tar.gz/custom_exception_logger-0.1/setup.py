from setuptools import setup, find_packages

setup(
    name='custom_exception_logger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            # Add any command line scripts here
        ],
    },
)
