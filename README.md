# FEWS OpenAPI Python Client

A Python client library for accessing the Delft-FEWS Web Services REST API v1. This library provides a type-safe, auto-generated interface to interact with FEWS (Flood Early Warning System) web services.

## Table of contents

- [Features](#features)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [From Source](#from-source)
  - [Using UV](#using-uv)
- [Usage](#usage)
  - [Basic Example](#basic-example)
  - [Async Example](#async-example)
  - [Client Configuration](#client-configuration)
- [Contributing and releases](#contributing-and-releases)

## Features

- **Type-safe**: Fully typed Python client with type hints
- **Auto-generated**: Generated from the official FEWS OpenAPI specification
- **Async support**: Both synchronous and asynchronous API calls
- **Comprehensive**: Covers all FEWS REST API v1 endpoints including:
  - Time series data
  - Archive operations
  - Display groups and filters
  - Parameters, locations, and qualifiers
  - Workflow and task management
  - And much more

## Installation

### From PyPI

```bash
uv add fews-openapi-py-client
```

or:

```bash
pip install fews-openapi-py-client
```

### From Source

Clone the repository and install the generated client:

```bash
cd fews-openapi-py-client
uv pip install -e .
```

### Using UV

```bash
uv add ./fews-openapi-py-client
```

## Usage

### Basic Example

```python
from fews_openapi_py_client import Client
from fews_openapi_py_client.api.timeseries import timeseries

# Create a client
client = Client(base_url="https://your-fews-server.com/FewsWebServices")

# Fetch time series data
response = timeseries.sync_detailed(
    client=client,
    filter_id="your_filter_id",
    location_ids="location1,location2",
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-01-31T23:59:59Z"
)

if response.status_code == 200:
    data = response.parsed
    # Process your time series data
```

### Async Example

```python
import asyncio
from fews_openapi_py_client import Client
from fews_openapi_py_client.api.timeseries import timeseries

async def fetch_data():
    client = Client(base_url="https://your-fews-server.com/FewsWebServices")

    response = await timeseries.asyncio_detailed(
        client=client,
        filter_id="your_filter_id",
        location_ids="location1,location2",
        start_time="2024-01-01T00:00:00Z",
        end_time="2024-01-31T23:59:59Z"
    )

    return response.parsed

# Run the async function
data = asyncio.run(fetch_data())
```

### Client Configuration

Configure the client with custom settings:

```python
from fews_openapi_py_client import Client

client = Client(
    base_url="https://your-fews-server.com/FewsWebServices",
    timeout=30.0,  # Request timeout in seconds
    verify_ssl=True,  # SSL certificate verification
    headers={
        "Authorization": "Bearer your_token",
        "Custom-Header": "value"
    }
)
```

## Contributing and releases

Development, client generation, post-processing, and PyPI release instructions are documented in [CONTRIBUTING.md](CONTRIBUTING.md).
