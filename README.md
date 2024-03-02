# Test poetry python references

This project is a test to implement three python projects (poetrytest, dep1 and dep2) that depend on each other in a chain. Each of them is packaged as a local python package and has a pyproject.toml file. It uses [poetry](https://python-poetry.org/) for resolving the relative references.

All three projects can be installed in a new python venv by these commands:

```
# Create venv
python3 -m venv nameOfMyVenv

# Activate venv
source ./nameOfMyVenv/bin/activate

# Install project
pip install ./poetrytest

# Call the Script
meinscri

# Deactivate venv
deactivate

# Remove venv
rm -r nameOfMyVenv
```

This project also addes an .vscode folder with an launch.json file. This makes it possible to run and debug the code from within visual studio code without the need of installing and updating the pip packages.
It works by updating the pythonpath environment variable which has to hold all the referenced libraries source paths (./dep1 and ./dep2 in this case).
