from setuptools import setup, find_packages

setup(
    name='SafePassGen',
    version='1.0.6',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'SafePassGen=secure_password.__main__:main',
        ],
    },
    author='Diego Mengarelli',
    description='A package to generate secure passwords with customizable options and check vulnerability and strength',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/diegoamengarelli/passgenesis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.9',
)