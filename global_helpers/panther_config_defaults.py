"""
Here, default values for `panther_config.config` are defined
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ipaddress import IPv4Network, IPv6Network

# A list of public DNS domain names that fall under the administrative domain of
# the Panther installation
ORGANIZATION_DOMAINS = ["example.com"]

DROPBOX_ALLOWED_SHARE_DOMAINS = ORGANIZATION_DOMAINS
DROPBOX_TRUSTED_OWNERSHIP_DOMAINS = ORGANIZATION_DOMAINS
GSUITE_TRUSTED_FORWARDING_DESTINATION_DOMAINS = ORGANIZATION_DOMAINS
GSUITE_TRUSTED_OWNERSHIP_DOMAINS = ORGANIZATION_DOMAINS
MS_EXCHANGE_ALLOWED_FORWARDING_DESTINATION_DOMAINS = ORGANIZATION_DOMAINS
MS_EXCHANGE_ALLOWED_FORWARDING_DESTINATION_EMAILS = ["postmaster@" + ORGANIZATION_DOMAINS[0]]
TELEPORT_ORGANIZATION_DOMAINS = ORGANIZATION_DOMAINS

DMZ_NETWORKS: list[Union[IPv4Network, IPv6Network]] = [
    # ip_network("10.1.0.0/24"),
]

DMZ_TAGS = {
    ("environment", "dmz"),
}

PCI_NETWORKS: list[Union[IPv4Network, IPv6Network]] = [
    # ip_network("10.0.0.0/24"),
]
