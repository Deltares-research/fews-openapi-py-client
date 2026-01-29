# FEWS OpenAPI Python Client

A Python client library for accessing the Delft-FEWS Web Services REST API v1. This library provides a type-safe, auto-generated interface to interact with FEWS (Flood Early Warning System) web services.

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

## Development

## Generate the open api client

To generate the openapi client use the following command:

```bash
uv run openapi-python-client generate --url https://fewsdocs.deltares.nl/webservices/rest-api/v1/delft-fews-webservices-rest-api-v1-oas3.json --config config.yml --overwrite
```

Then run the postprocess script to replace the occurrences of datetime.datedatime and datetime.datedatime.isoformat() calls with str. Otherwise the formatting will break the FEWS api.

```bash
uv run python scripts/postprocess_client.py
```

## Customizing the Post Process Script

The post process script ([scripts/postprocess_client.py](scripts/postprocess_client.py)) allows you to apply custom code transformations to the generated client files. You can customize it by modifying two main configuration variables:

### Adding Files to Process

Add file paths to the `FILES_TO_PROCESS` list. Paths are relative to `fews-openapi-py-client/fews_openapi_py_client/`:

```python
FILES_TO_PROCESS = [
    "api/timeseries/timeseries.py",
    "api/other/module.py",  # Add more files here
]
```

### Adding Replacement Patterns

Add regex patterns to the `REPLACEMENT_PATTERNS` dictionary. The key is the regex pattern to match, and the value is the replacement string:

```python
REPLACEMENT_PATTERNS = {
    r"(\w+)\.isoformat\(\)": r"\1",  # Remove isoformat calls
    r"datetime\.datetime": r"str",  # Replace datetime.datetime with str
    r"YourPattern": r"YourReplacement",  # Add custom patterns here
}
```

The script uses Python's `re.sub()` function, so you can use capture groups (e.g., `\1`, `\2`) in your replacement strings to reference matched groups from the pattern.
