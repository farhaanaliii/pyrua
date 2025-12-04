"""
pyrua - Professional Random User-Agent Generator

A comprehensive Python module for generating realistic User-Agent strings
for web scraping, testing, and browser simulation purposes.

Basic Usage:
    >>> from pyrua import get_rua
    >>> user_agent = get_rua()
    
Advanced Usage:
    >>> from pyrua import get_ua, Browser, OS, DeviceType
    >>> ua = get_ua(browser=Browser.CHROME, os_type=OS.WINDOWS)
    >>> mobile_ua = get_ua(device_type=DeviceType.MOBILE)
"""

from .pyrua import (
    # Main functions
    get_rua,
    get_ua,
    get_rua_list,
    get_common_ua,
    
    # Browser-specific functions
    get_chrome_ua,
    get_firefox_ua,
    get_safari_ua,
    get_edge_ua,
    get_opera_ua,
    
    # Device-specific functions
    get_desktop_ua,
    get_mobile_ua,
    get_android_ua,
    get_ios_ua,
    
    # Legacy support
    get_legacy_ua,
    
    # Enums for customization
    Browser,
    OS,
    DeviceType,
)

__author__ = "Farhan Ali"
__version__ = "1.0.0"
__github__ = "https://github.com/farhaanaliii/pyrua"
__license__ = "MIT"
__description__ = "Professional Random User-Agent Generator for Python"

__all__ = [
    # Main functions
    "get_rua",
    "get_ua",
    "get_rua_list",
    "get_common_ua",
    
    # Browser-specific functions
    "get_chrome_ua",
    "get_firefox_ua",
    "get_safari_ua",
    "get_edge_ua",
    "get_opera_ua",
    
    # Device-specific functions
    "get_desktop_ua",
    "get_mobile_ua",
    "get_android_ua",
    "get_ios_ua",
    
    # Legacy support
    "get_legacy_ua",
    
    # Enums
    "Browser",
    "OS",
    "DeviceType",
]
