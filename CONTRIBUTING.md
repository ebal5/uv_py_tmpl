# Contributing

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/your_project_name.git`
3. Set up the development environment:

```bash
cd your_project_name
uv venv
uv sync --editable ".[dev]"
uv add pre-commit
pre-commit install
```

## Code Style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting. 
To ensure your code follows the project's style, run:

```bash
uv run ruff check .
uv run ruff format .
```

## Type Checking

We use [mypy](https://mypy.readthedocs.io/) for static type checking:

```bash
uv run mypy src tests
```

## Testing

Write tests for your changes and ensure all tests pass:

```bash
uv run pytest
```

To run tests with coverage:

```bash
uv run pytest --cov=src --cov-report=term --cov-report=html
```

## Pull Request Process

1. Create a new branch for your changes
2. Make your changes
3. Add or update tests as needed
4. Update documentation as needed
5. Run tests, type checking, and linting to make sure everything passes
6. Push your changes and create a pull request

## Adding Dependencies

When adding dependencies:

1. Add runtime dependencies to `pyproject.toml` under `[project.dependencies]`
2. Add development dependencies to `pyproject.toml` under `[project.optional-dependencies.dev]`

## Documentation

If you change functionality, please update the documentation:

1. Update docstrings in the code
2. Update `README.md` if needed
3. Update or add to the documentation in the `docs` directory

## Commit Messages

Please use clear and meaningful commit messages. Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification when possible:

```
feat: add new feature
fix: correct bug in X
docs: update installation instructions
test: add tests for feature Y
refactor: reorganize code structure
```

## Updating the Changelog

Please add an entry to `CHANGELOG.md` under the `[Unreleased]` section for any notable changes:

- New features
- Bug fixes
- Documentation changes
- Performance improvements
- Notable refactorings

## Questions?

If you have any questions about contributing, please open an issue for discussion.