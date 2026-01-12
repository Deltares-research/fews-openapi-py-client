
To generate the openapi client use the following command:

```bash
poetry run openapi-python-client generate --url https://fewsdocs.deltares.nl/webservices/rest-api/v1/delft-fews-webservices-rest-api-v1-oas3.json --config config.yml --overwrite
```

Then run the postprocess script to replace the occurrences of datetime.datedatime and datetime.datedatime.isoformat() calls with str. Otherwise the formatting will break the FEWS api.

```bash
poetry run python scripts/postprocess_client.py
```
