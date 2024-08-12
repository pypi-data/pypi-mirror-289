from setuptools import setup, find_packages

setup(
    name='picassocli',  # Name of your package
    version='1.0.0',       # Version of your package
    description='A utility for constructing ANSI escape codes for terminal text styling.',
    long_description=open('README.md').read(),  # Long description from README file
    long_description_content_type='text/markdown',
    author='devinci-it',
    url='https://www.github.com/devinci-it/picassocli',  # Replace with your repo URL
    packages=find_packages(),  # List of packages to be included in the distribution),
    package_dir={'': '.'},  
    install_requires=[
        'huefy',  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',  # Specify Python versions supported
)
