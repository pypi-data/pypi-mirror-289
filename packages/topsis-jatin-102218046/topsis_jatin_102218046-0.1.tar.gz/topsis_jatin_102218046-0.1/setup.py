from setuptools import setup, find_packages

setup(
    name='topsis-jatin-102218046',
    version='0.1',
    author='Jatin Sharma',
    author_email='jatinsh596@gmail.com',
    description='A Python package for TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis-jatin-102218046 = topsis_jatin_102218046.topsis:main'
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

