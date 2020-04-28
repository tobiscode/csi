# Classic Slip Inversion

## Installation

### Prerequisites

#### General packages

CSI relies on a lot of amazing libraries written by smart people. Please install the following packages before continuing:

- Python 3
- NumPy
- SciPy
- Matplotlib
- Cartopy
- `pyproj`
- `h5py`
- `okada4py` (will be automatically installed by CSI if not present)

You can use `conda` (or similarly `pip`) to install all packages (except `okada4py`) with one simple command. If you have different virtual environments, make sure to activate the correct one first.

```bash
conda install python=3 numpy scipy matplotlib cartopy pyproj h5py
```

#### C++ Compiler

CSI is requiring `okada4py`, which in turn requires a C++ compiler (for example as part of the GNU Compiler Collection GCC) during installation. The CSI installation script will automatically check for the `okada4py` package, and if not found, try to install it directly from its [Github repository](<https://github.com/jolivetr/okada4py>) (manual installation instructions can also be found there). The `okada4py` installation will fail if no compiler is found.

You can check if you have GCC installed by running (for a `bash` shell):

```bash
which gcc
```

If it returns a path, `gcc` is installed on your system. Otherwise, you'll have to install it through a package manager like `apt`, `homebrew`, `macports`, `cygwin`, `mingw` etc.

### Installing CSI

Once all prerequisites are met (and if applicable, the correct environment is activated), you can use the following `pip` one-liner to automatically install CSI from the Github repository. It will also install `okada4py` if it's not installed already.

```bash
pip install csi@git+https://github.com/jolivetr/csi
```

If you want to keep the downloaded repository handy, you can also first clone the repository into a local folder, and then install it from there:

```bash
git clone https://github.com/jolivetr/csi.git
cd csi/
pip install .
```

You can easily uninstall CSI using `pip uninstall csi`.

#### Alternative installation

**Before procedding, make sure all requirements are fulfilled!**

If you don't want to use `pip`, you can alternatively just add the `src/` directory from the repository to your PYTHONPATH environment variable. For instance, in `bash`, add the following to your `.bashrc` or `.bash_profile`:

```bash
export PYTHONPATH=/path/to/csi/src:$PYTHONPATH
```

## Documentation

For a manual, installation instructions and some examples, please visit: <https://www.geologie.ens.fr/~jolivet/csi>.
