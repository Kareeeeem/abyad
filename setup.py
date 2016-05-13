import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Laysa',
    version='0.0.1',
    description='A Whitespace interpreter.',
    long_description=read('README.md'),
    author='Mohammed Kareem',
    author_email='kareeeeem@gmail.com',
    license='MIT',
    # packages=find_packages(),
    packages=['src'],
    install_requires=[
        'pytest'
    ],
    entry_points="""
        [console_scripts]
    """,
)

