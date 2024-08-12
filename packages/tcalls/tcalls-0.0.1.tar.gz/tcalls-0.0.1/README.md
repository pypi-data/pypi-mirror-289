# LLMs tool calling


## Quick Install
With pip:
```
pip install -U tcalls
```

## Contributing

To set up the project with [poetry](https://python-poetry.org):
:
```bash
git clone https://github.com/onemquan/tcalls.git

cd tcalls
pip install poetry
poetry env use python3.10  # make sure python --version ~ 3.10
poetry shell

# install test/develop dependencies
poetry install
poetry run pre-commit install

# run tests:
poetry run pytest
```
The full [contributing documentation](./CONTRIBUTING.md) provides helpful guidance.
