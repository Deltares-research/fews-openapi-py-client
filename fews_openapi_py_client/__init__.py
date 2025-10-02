"""A client library for accessing Delft-FEWS Web Services REST API v1"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
