# Classic Slip Inversion

## Installation

### Prerequisites

CSI relies on a lot of amazing libraries written by smart people. Please install the following packages before continuing:

- Python 3
- NumPy
- SciPy
- Matplotlib
- Cartopy
- `pyproj`
- `h5py`
- `okada4py`

For everything except `okada4py`, you can use `conda` (or similarly `pip`). If you have different virtual environments, make sure to activate the correct one first.

```bash
conda install python=3 numpy scipy matplotlib cartopy pyproj h5py
```

### Installing `okada4py`

*This is a slight adaptation of <https://github.com/jolivetr/okada4py>.*

First, clone the repository:

```bash
cd my_downloads_folder/
git clone https://github.com/jolivetr/okada4py.git
```

Then use `pip` to compile the needed files and install them into your current Python installation (or active `conda` environment):

```bash
cd okada4py/
pip install .
```

You can test `okada4py` by running `python test/test.py`. If you want to uninstall it, use `pip uninstall okada4py` (make sure you are in the correct environment). If you don't want to use `pip`, follow the instructions on the `okada4py` website.

### Installing CSI

First, clone the repository:

```bash
cd my_downloads_folder/
git clone https://github.com/jolivetr/csi.git
```

Then use `pip` to install it into your current Python installation (or active `conda` environment):

```bash
cd git/
pip install .
```

Just like `okada4py`, you can easily uninstall it using `pip uninstall csi`.

#### Alternative installation

If you don't want to use `pip`, you can alternatively just add the `src/` directory from the repository to your PYTHONPATH environment variable. For instance, in `bash`, add the following to your `.bashrc` or `.bash_profile`:

```bash
export PYTHONPATH=/path/to/csi/src:$PYTHONPATH
```

## Documentation

For a manual, installation instructions and some examples, please visit: <https://www.geologie.ens.fr/~jolivet/csi>.
