__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "11.08.2024"
__email__ = "m@hler.eu"
__status__ = "Development"

import re
import urllib.parse
from typing import Optional


def link_type(inspect: str) -> Optional[str]:
    """Get the type of inspect link (masked or unmasked)"""

    link_valid, link_type_str = is_link_valid(inspect)
    if link_valid:
        return link_type_str

    return None


def is_link_valid(inspect: str) -> tuple[bool, Optional[str]]:
    """Validate a given inspect link"""

    if not is_link_quoted(inspect):
        inspect = quote_link(inspect)

    unmasked = re.compile(r"^steam://rungame/730/\d+/[+ ]csgo_econ_action_preview(?: ?|%20)([SM])(\d+)A(\d+)D(\d+)$")
    masked = re.compile(r"^steam://rungame/730/\d+/[+ ]csgo_econ_action_preview(?: ?|%20)[0-9A-F]+$")
    patterns = {
        'unmasked': unmasked,
        'masked': masked
    }

    for link_type_str, pattern in patterns.items():
        if pattern.search(inspect):
            return True, link_type_str

    return False, None


def is_link_quoted(inspect: str) -> bool:
    """Check if an inspect link is url encoded"""
    return "%20" in inspect


def unquote_link(inspect: str) -> str:
    """Unquote the given inspection link"""

    return urllib.parse.unquote(inspect)


def quote_link(inspect: str) -> str:
    """Quote the given inspection link (this is inspect link specific!)"""

    return urllib.parse.quote(inspect, safe=":/+")


if __name__ == '__main__':
    exit(1)
