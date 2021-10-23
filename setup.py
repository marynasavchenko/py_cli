from setuptools import setup

setup(
    name='py_cli',
    version='1.0.0',
    packages=['py_cli'],
    entry_points={
        'console_scripts': [
            'py_cli = py_cli.__main__:main'
        ]
    })
