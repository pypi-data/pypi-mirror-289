from setuptools import setup, find_packages

setup(
    name='topsis-sidharth-102218069',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    author='Sidharth Dhawan',
    author_email='sidharthdhawan17@gmail.com',
    description='A Python package to perform TOPSIS analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sidharthd7/Topsis-Sidharth-102218069',
    license='MIT',
)
