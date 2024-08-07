from setuptools import setup, find_packages

setup(
    name='pathdirector',
    version='0.0.1',
    url='https://github.com/naveensagar765/pathdirector',
    license='MIT',
    author='Naveen Sagar',
    author_email='sagarnaveen886@gmail.com',
    description='Path director is simple python package for getting/creating application/downloads/tempdir paths ',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.6',
)
