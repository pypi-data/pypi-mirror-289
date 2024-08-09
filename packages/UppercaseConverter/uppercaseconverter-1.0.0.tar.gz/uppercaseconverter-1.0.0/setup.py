from setuptools import setup, find_packages

setup(
    name='UppercaseConverter',
    version='1.0.0',
    packages=find_packages(),
    description='A simple package to convert file content to uppercase',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sidharth Dhawan',
    author_email='sidharthdhawan17@gmail.com',
    url='https://github.com/sidharthd7/UppercaseConverter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['python', 'converter', 'lower to upper', 'uppercase converter', 'uppercase', 'textfile'],
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'convert-to-upper=uppercase_converter.converter:main',
        ],
    },
)
