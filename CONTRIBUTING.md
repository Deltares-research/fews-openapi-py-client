# Contributing

This document contains development, client generation, post-processing, and release instructions for maintainers and contributors.

## Table of contents

- [Development](#development)
- [Generate the OpenAPI client](#generate-the-openapi-client)
- [Customizing the post-process script](#customizing-the-post-process-script)
  - [Adding files to process](#adding-files-to-process)
  - [Adding replacement patterns](#adding-replacement-patterns)
- [Publishing to PyPI](#publishing-to-pypi)

## Development

Install development dependencies with:

```bash
uv sync --extra dev
```

## Generate the OpenAPI client

To generate the OpenAPI client, use the following command:

```bash
uv run openapi-python-client generate --url https://fewsdocs.deltares.nl/webservices/rest-api/v1/delft-fews-webservices-rest-api-v1-oas3.json --config config.yml --overwrite
```

Then run the post-process script to replace occurrences of `datetime.datetime` and `datetime.datetime.isoformat()` calls with `str`. Otherwise, the formatting will break the FEWS API.

```bash
uv run python scripts/postprocess_client.py
```

## Customizing the post-process script

The post-process script ([scripts/postprocess_client.py](scripts/postprocess_client.py)) allows you to apply custom code transformations to the generated client files. You can customize it by modifying two main configuration variables.

### Adding files to process

Add file paths to the `FILES_TO_PROCESS` list. Paths are relative to `fews-openapi-py-client/fews_openapi_py_client/`:

```python
FILES_TO_PROCESS = [
    "api/timeseries/timeseries.py",
    "api/other/module.py",  # Add more files here
]
```

### Adding replacement patterns

Add regex patterns to the `REPLACEMENT_PATTERNS` dictionary. The key is the regex pattern to match, and the value is the replacement string:

```python
REPLACEMENT_PATTERNS = {
    r"(\w+)\.isoformat\(\)": r"\1",  # Remove isoformat calls
    r"datetime\.datetime": r"str",  # Replace datetime.datetime with str
    r"YourPattern": r"YourReplacement",  # Add custom patterns here
}
```

The script uses Python's `re.sub()` function, so you can use capture groups (for example, `\1` or `\2`) in replacement strings to reference matched groups from the pattern.

## Publishing to PyPI

This repository publishes to PyPI from GitHub Actions when a tag starting with `version` is pushed.

Before the first release:

1. Create the project on PyPI, or reserve the name by publishing the first release.
2. Configure a PyPI Trusted Publisher for this GitHub repository with:
   - Workflow: `.github/workflows/publish-to-pypi.yml`
   - Environment: `pypi`
3. Ensure the version in `pyproject.toml` is the version you want to publish.

To publish a release:

```bash
git checkout main
git pull
git tag version0.1.0
git push origin version0.1.0
```

The workflow verifies that the tagged commit is on `main`, builds the source distribution and wheel, checks the package metadata, and publishes the artifacts to PyPI.

