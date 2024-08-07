# hyclib
A personal python package containing commonly used functions within my projects.

# Install
`pip install hyclib`

If you're developing the package, then clone/fork the package, and in the top level directory of the repository do

`pip install -r requirements.txt`

Since this package requires pytorch, if you're on a linux system and want a cpu-only version of pytorch, you can instead do

`pip install -r requirements_linux_cpu.txt`

Note: If you're on M1 Mac, there's a problem with pytables version 3.8.0 (as of writing) that you might encounter during install in which it complains it cannot find hdf5 install. If that is the case, then do

`export HDF5_DIR=/opt/homebrew/opt/hdf5`

you can put this line in your `~/.bashrc` file for convenience.