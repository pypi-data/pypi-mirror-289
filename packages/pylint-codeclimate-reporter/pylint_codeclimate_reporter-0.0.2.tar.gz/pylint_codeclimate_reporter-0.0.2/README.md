# Pylint Code Climate Reporter

This Pylint reporter generates reports in Code Climate compatible JSON format.
This is useful for integration of Pylint with tools such as GitLab CI.

## Installation

Pylint Code Climate Reporter is published on PyPI and can be installed from
there.

```
pip install pylint-codeclimate-reporter
```

## Usage

Place the following in `.pylintrc`:

```
[MASTER]
load-plugins=pylint_codeclimate_reporter

[REPORTS]
output-format=pylint_codeclimate_reporter.CodeClimateReporter
```

or place the following in `pyproject.toml`:

```
[tool.pylint.MASTER]
load-plugins = "pylint_codeclimate_reporter"

[tool.pylint.REPORTS]
output-format= "pylint_codeclimate_reporter.CodeClimateReporter"
```

or manually pass the `--load-plugins` and `--output-format` flags when calling
pylint.
