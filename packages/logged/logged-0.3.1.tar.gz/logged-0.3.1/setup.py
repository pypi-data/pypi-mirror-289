from setuptools import setup, find_packages

setup(
    name='logged',
    version='0.3.1',
    packages=find_packages(),
    install_requires=[
        "datetime"
    ],
    entry_points={
        'console_scripts': [
            # If you have command-line scripts
        ],
    },
    author='hypixeloffical',
    author_email='hypixel.offical.tr@gmail.com',
    description='A custom logging package with advanced features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hypixeloffical/logged-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
