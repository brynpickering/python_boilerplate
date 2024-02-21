
# Installation

## Setting up a user environment

As a `python_boilerplate` user, it is easiest to install using the [mamba](https://mamba.readthedocs.io/en/latest/index.html) package manager, as follows:

1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
1. Open the command line (or the "miniforge prompt" in Windows).
1. Download (a.k.a., clone) the python_boilerplate repository: `git clone git@github.com:arup-group/python_boilerplate.git`
1. Change into the `python_boilerplate` directory: `cd python_boilerplate`
1. Create the python_boilerplate mamba environment: `mamba create -n python_boilerplate -c conda-forge -c city-modelling-lab --file requirements/base.txt`
1. Activate the python_boilerplate mamba environment: `mamba activate python_boilerplate`
1. Install the python_boilerplate package into the environment, ignoring dependencies (we have dealt with those when creating the mamba environment): `pip install --no-deps .`


All together:

--8<-- "README.md:docs-install-user"

### Running the example notebooks

If you have followed the non-developer installation instructions above, you will need to install `jupyter` into your `python_boilerplate` environment to run the [example notebooks](https://github.com/arup-group/python_boilerplate/tree/main/examples):

``` shell
mamba install -n python_boilerplate jupyter
```

With Jupyter installed, it's easiest to then add the environment as a jupyter kernel:

``` shell
mamba activate python_boilerplate
ipython kernel install --user --name=python_boilerplate
jupyter notebook
```

### Choosing a different environment name

If you would like to use a different name to `python_boilerplate` for your mamba environment, the installation becomes (where `[my-env-name]` is your preferred name for the environment):

``` shell
mamba create -n [my-env-name] -c conda-forge --file requirements/base.txt
mamba activate [my-env-name]
ipython kernel install --user --name=[my-env-name]
```

## Setting up a development environment

The install instructions are slightly different to create a development environment compared to a user environment:

--8<-- "README.md:docs-install-dev"

For more detailed installation instructions specific to developing the python_boilerplate codebase, see our [development documentation][setting-up-a-development-environment].
