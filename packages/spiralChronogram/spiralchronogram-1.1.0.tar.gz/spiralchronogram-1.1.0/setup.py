from setuptools import setup, find_packages

setup(
    name='spiralChronogram',   
    version='1.1.0',
    description='A package to generate various types of 2D representations of data and spiral chronograms.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jcevall1/spiralChronogram',   
    author='IMSI2024',
    author_email='jcevall1@asu.edu',
    license='CC BY-SA 4.0',   
    install_requires=[
        'numpy==1.23.1',
        'pandas==1.4.3',
        'matplotlib==3.5.2',
        'seaborn==0.11.2',
        'scipy==1.8.1',
        'plotly==5.23.0',
        'biopython==1.84',
        'ipython==8.26.0'
    ],
    entry_points={
        'console_scripts': [
            'spiralChronogram=spiralChronogram.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
