from setuptools import setup, find_packages

setup(
    name='venvwatch',
    version='0.3',
    description='Automatically updates requirements.txt by watching your virtual environment for changes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'venvwatch = venvwatch.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
