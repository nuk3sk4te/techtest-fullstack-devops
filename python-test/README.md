# Configure virtual environment

Example:

python3 -m venv pytest
source pytest/bin/activate

# Install and Configure pytest

## Installation

To install `pytest`, you can use `pip`. Run the following command in your terminal:

```sh
pip install pytest
```

## Configuration

To configure `pytest`, you can create a `pytest.ini` file in the root of your project directory. Here is an example configuration:

```ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
```

- `minversion`: Specifies the minimum version of `pytest` required.
- `addopts`: Additional command-line options to pass to `pytest`.
- `testpaths`: Directories to search for tests.

## Running Tests

To run your tests, simply execute the following command in your terminal:

```sh
pytest
```

This will discover and run all the tests in the specified `testpaths`.

For more information, refer to the [pytest documentation](https://docs.pytest.org/en/stable/).
