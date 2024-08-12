from setuptools import setup, find_packages

setup(
    name='rafidimg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'seaborn',
        'scipy',
        'numpy'
    ],
    description='A package to extract dominant colors from images.',
    author='Rafid Hasan',
    author_email='rafid.dejrah@gmail.com',
    url='https://rafid-hasan.com/',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
)

