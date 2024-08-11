from setuptools import setup, find_packages

setup(
    name='algods',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={'console_scripts': [],},
    author='Ananyo Bhattacharya',
    author_email='ananyobhattacharya10@gmail.com',
    description='A Python package for data structures and algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/UniquePython/Algods',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
