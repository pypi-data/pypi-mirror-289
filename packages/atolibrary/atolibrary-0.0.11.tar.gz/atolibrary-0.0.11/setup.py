from setuptools import setup, find_packages

setup(
    name="atolibrary",
    version="0.0.11",
    author="ATO JEON",
    author_email="atto.jeon@gmail.com",
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.0',
        'requests',
        'faker',
    ],
)
