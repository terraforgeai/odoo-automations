"""
Odoo API Connection Script
Connects to Odoo using XML-RPC and authenticates with credentials.
"""

import xmlrpc.client
from dataclasses import dataclass


@dataclass
class OdooConfig:
    """Configuration for Odoo connection."""
    url: str
    database: str
    username: str
    password: str  # Can be password or API key


class OdooAPI:
    """Handles connection and authentication to Odoo via XML-RPC."""

    def __init__(self, config: OdooConfig):
        self.config = config
        self.uid = None
        self._common = None
        self._models = None

    @property
    def common(self):
        """Lazy-load common endpoint."""
        if self._common is None:
            self._common = xmlrpc.client.ServerProxy(
                f"{self.config.url}/xmlrpc/2/common"
            )
        return self._common

    @property
    def models(self):
        """Lazy-load models endpoint."""
        if self._models is None:
            self._models = xmlrpc.client.ServerProxy(
                f"{self.config.url}/xmlrpc/2/object"
            )
        return self._models

    def authenticate(self) -> int:
        """
        Authenticate with Odoo and return user ID.

        Returns:
            int: User ID if authentication successful

        Raises:
            Exception: If authentication fails
        """
        self.uid = self.common.authenticate(
            self.config.database,
            self.config.username,
            self.config.password,
            {}
        )

        if not self.uid:
            raise Exception("Authentication failed. Check your credentials.")

        print(f"Successfully authenticated as user ID: {self.uid}")
        return self.uid

    def get_version(self) -> dict:
        """Get Odoo server version info."""
        return self.common.version()

    def execute(self, model: str, method: str, *args, **kwargs):
        """
        Execute a method on an Odoo model.

        Args:
            model: The Odoo model name (e.g., 'res.partner')
            method: The method to call (e.g., 'search', 'read', 'create')
            *args: Positional arguments for the method
            **kwargs: Keyword arguments for the method

        Returns:
            The result of the method call
        """
        if self.uid is None:
            raise Exception("Not authenticated. Call authenticate() first.")

        return self.models.execute_kw(
            self.config.database,
            self.uid,
            self.config.password,
            model,
            method,
            args,
            kwargs
        )

    def search(self, model: str, domain: list, **kwargs):
        """Search for record IDs matching the domain."""
        return self.execute(model, 'search', domain, **kwargs)

    def read(self, model: str, ids: list, fields: list = None):
        """Read records by IDs."""
        return self.execute(model, 'read', ids, fields or [])

    def search_read(self, model: str, domain: list, fields: list = None, **kwargs):
        """Search and read records in one call."""
        return self.execute(model, 'search_read', domain, fields=fields or [], **kwargs)

    def create(self, model: str, values: dict):
        """Create a new record."""
        return self.execute(model, 'create', values)

    def write(self, model: str, ids: list, values: dict):
        """Update existing records."""
        return self.execute(model, 'write', ids, values)

    def unlink(self, model: str, ids: list):
        """Delete records."""
        return self.execute(model, 'unlink', ids)


def main():
    # Example usage - replace with your actual credentials
    config = OdooConfig(
        url="https://fwapparel.odoo.com",
        database="fwapparel",
        username="fwapparel@protonmail.com",
        password="YOUR_API_KEY_HERE"
    )

    api = OdooAPI(config)

    # Get server version (no auth required)
    version = api.get_version()
    print(f"Odoo Server Version: {version.get('server_version')}")

    # Authenticate
    api.authenticate()

    # Example: Search for partners
    partners = api.search_read(
        'res.partner',
        domain=[('is_company', '=', True)],
        fields=['name', 'email', 'phone'],
        limit=5
    )

    print("\nFirst 5 company partners:")
    for partner in partners:
        print(f"  - {partner['name']}")


if __name__ == "__main__":
    main()
