from setuptools import setup, find_packages

setup(
    name='0xdirsan',
    version='0.0.6',
    author='x-projetion',
    author_email='lutfifakee@proton.me',
    description='0xdirsan is a simple program designed to search for directories within the file system using brute-force with a given list of words.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={
        'xdirsan': ['wordlist/*.txt'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'xdirsan=xdirsan.main:main',
        ],
    },
    install_requires=[
        'requests',
        'colorama',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
