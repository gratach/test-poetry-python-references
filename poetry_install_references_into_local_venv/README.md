This project defines a simple Python script that references the package `cowsay` from the Python Package Index.
The script can be installed using poetry.

## Installation

Navigate into this directory and run the following command:
```
poetry install
```
The settings in the poetry.toml file will result in a local venv being created in the directory `./.venv`.

The installation will also create a poetry.lock file that contains the exact versions of the installed packages and should usually be commited to the repository.

## Alternative Installation

The package can also be installed using pip install.
In this case the venv has to be created manually.

Navigate into this directory and run the following command:
```
python3 -m venv .venv
```

The venv has to be activated before the script can be run. This can be done by running the following command:
```
source ./.venv/bin/activate
```

Install the package by running the following command:
```
pip install .
```

## Usage

The venv has to be activated before the script can be run. This can be done by running the following command:
```
source ./.venv/bin/activate
```

The script can then be run by executing the following command:
```
python3 -m localvenvtest
```

The venv can be deactivated by running the following command:
```
deactivate
```