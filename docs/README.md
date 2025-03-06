# Documentation

This directory contains the project documentation.

## Building the docs

Install the documentation dependencies:

```bash
uv sync --editable ".[docs]"
```

Then build the documentation:

```bash
cd docs
sphinx-build -b html . _build/html
```

The documentation will be available in the `_build/html` directory.

## Setting up CodeQL

This project is ready for CodeQL scanning, which you can enable directly through the GitHub UI:

1. Go to your repository on GitHub
2. Click on **Security** tab
3. Click on **Code scanning**
4. Select **Configure CodeQL alerts**
5. Select **Default** setup

GitHub will automatically configure and run CodeQL analysis for your Python code without requiring any workflow files. This provides:

- Automatic language detection
- Optimal query selection
- Regular scheduled scans
- Scan results in the Security tab