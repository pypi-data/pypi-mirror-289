from setuptools import setup, find_packages

setup(
    name='hotkey',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here
        ],
    },
    author='Dominik Bilski',
    author_email='dominik.bilski42@gmail.com',
    description='This is a package for hoykeys',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bilski311/hotkey',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)