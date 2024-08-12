from setuptools import setup, find_packages

setup(
    name='pip_sdk_build_test',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pip-sdk-build-test=pip_sdk_build_test.main:main',
        ],
    },
)

