# Project Name

[![Tests](https://github.com/yourusername/your_project_name/actions/workflows/test.yml/badge.svg)](https://github.com/yourusername/your_project_name/actions/workflows/test.yml)
[![Lint](https://github.com/yourusername/your_project_name/actions/workflows/lint.yml/badge.svg)](https://github.com/yourusername/your_project_name/actions/workflows/lint.yml)
[![Type Check](https://github.com/yourusername/your_project_name/actions/workflows/type-check.yml/badge.svg)](https://github.com/yourusername/your_project_name/actions/workflows/type-check.yml)
[![CodeQL](https://github.com/yourusername/your_project_name/github/code-scanning/workflows/codeql/badge.svg)](https://github.com/yourusername/your_project_name/security/code-scanning)
[![PyPI version](https://badge.fury.io/py/your_project_name.svg)](https://badge.fury.io/py/your_project_name)
[![Python Version](https://img.shields.io/pypi/pyversions/your_project_name.svg)](https://pypi.org/project/your_project_name/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Description of your project.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for package management.

```bash
# Install uv if you don't have it yet
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies
uv venv
uv sync  # Installs dependencies from pyproject.toml

# For development installation (editable mode)
uv venv
uv sync --editable .
```

## Usage

```python
from your_package_name import example_function

# Example code
result = example_function()
print(result)
```

## Development

```bash
# Install development dependencies
uv sync --editable ".[dev]"

# Install pre-commit hooks
uv add pre-commit
pre-commit install

# Run linting
uv run ruff check .

# Run formatting
uv run ruff format .

# Run type checking
uv run mypy src tests

# Run tests
uv run pytest

# Add a package to your project
uv add requests

# Update dependencies to latest compatible versions
uv sync --update
```

## Documentation

Documentation is available at [your_project_name.readthedocs.io](https://your_project_name.readthedocs.io).

To build the documentation locally:

```bash
uv sync --editable ".[docs]"
cd docs
sphinx-build -b html . _build/html
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure your code passes all tests, is formatted with Ruff, and includes appropriate type hints.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for details on recent changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.