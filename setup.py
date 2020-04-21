#!/usr/bin/env python

# imports
from os import path
from setuptools import setup
from setuptools.command.install import install


# define a custom installer that first checks if okada4py is installed
class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        try:
            import okada4py
            print(f"'okada4py' found at: {okada4py.__file__}")
        except ModuleNotFoundError:
            print("Could not import the 'okada4py' Python module, which is "
                  "a prerequisite for CSI. Please install it before proceeding, "
                  "and/or check for more debugging options by running Python and "
                  "trying to import it yourself.")
            raise
        install.run(self)


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
          package_dir={'csi': 'src'},
          packages=['csi'],
          cmdclass={'install': CustomInstallCommand},
          description='Classic Slip Inversion',
          long_description=long_description,
          long_description_content_type='text/markdown',
          classifiers=['Intended Audience :: Science/Research',
                       'Topic :: Scientific/Engineering',
                       'License :: OSI Approved :: MIT License',
                       'Programming Language :: Python :: 3'])
