#!/usr/bin/env python

# imports
from os import path
from setuptools import setup


if __name__ == "__main__":
    # load description from README.md
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    # run setup
    setup(name='csi',
          version='1.0',
          author='Romain Jolivet',
          author_email='romain.jolivet@ens.fr',
          url='https://www.geologie.ens.fr/~jolivet/csi/',
          download_url='https://github.com/jolivetr/csi',
          python_requires='>=3',
          install_requires=['numpy',
                            'scipy',
                            'matplotlib',
                            'cartopy',
                            'pyproj',
                            'h5py',
                            'okada4py @ git+https://github.com/jolivetr/okada4py.git'],
          package_dir={'csi': 'src'},
          packages=['csi'],
          description='Classic Slip Inversion',
          long_description=long_description,
          long_description_content_type='text/markdown',
          classifiers=['Intended Audience :: Science/Research',
                       'Topic :: Scientific/Engineering',
                       'License :: OSI Approved :: MIT License',
                       'Programming Language :: Python :: 3'])
