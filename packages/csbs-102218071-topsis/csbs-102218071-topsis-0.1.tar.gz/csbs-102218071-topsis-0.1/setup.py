from setuptools import setup, find_packages

setup(
    name='csbs-102218071-topsis',
    version='0.1',
    author='Sanchit2004',
    author_email='sanchitm990@gmail.com',
    description='A Python package for implementing the TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis=__main__:topsis',  # Ensure this matches the file name
        ],
    },
    install_requires=[
        'pandas',
        'numpy',
    ],
)
