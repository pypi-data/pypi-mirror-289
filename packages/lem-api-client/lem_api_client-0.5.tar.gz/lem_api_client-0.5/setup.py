from setuptools import setup, find_packages

setup(
    name='lem-api-client',
    version='0.5',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lem-api-client = LEMApiClient.api_client:main'
        ],
    },
)
