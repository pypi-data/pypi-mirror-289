from setuptools import setup, find_packages

setup(
    name='topsis-nikhil-102218082',
    version='0.1',
    author='Nikhil Gupta',
    author_email='nikhilgupta8235@gmail.com',
    description='A Python package for TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis-nikhil-102218082 = topsis_nikhil_102218082.topsis:main'
        ],
    },
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

