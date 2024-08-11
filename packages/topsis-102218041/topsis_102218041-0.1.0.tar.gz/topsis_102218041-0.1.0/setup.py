from setuptools import setup, find_packages

setup(
    name='topsis-102218041',  # The name of your package on PyPI
    version='0.1.0',  # Initial version
    description='A Python implementation of the TOPSIS method for multi-criteria decision making',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Eshitva',
    author_email='goyaleshitva@gmail.com',
    url='https://github.com/Eshitva/102218041_Eshitva_TOPSIS',  # Your repository URL
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.main_102218041:main',  # Entry point for your command-line tool
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
