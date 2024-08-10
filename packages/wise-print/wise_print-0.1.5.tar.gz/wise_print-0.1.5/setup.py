import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='wise_print',
    author='Daniele Dapuzzo',
    author_email='',
    description='Simple package to add info to print statements',
    keywords='print, pypi, package, logging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dandpz/wise_print',
    project_urls={
        'Documentation': 'https://github.com/dandpz/wise_print',
        'Bug Reports':
        'https://github.com/dandpz/wise_print/issues',
        'Source Code': 'https://github.com/dandpz/wise_print',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Debuggers',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    extras_require={
        'dev': ['check-manifest'],
    },
)
