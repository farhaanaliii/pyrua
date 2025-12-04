"""
pyrua - Professional Random User-Agent Generator

A comprehensive Python module for generating realistic User-Agent strings
for web scraping, testing, and browser simulation purposes.
"""

import random
import string
from typing import Optional, List, Literal
from enum import Enum


class Browser(Enum):
    """Supported browser types."""
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    EDGE = "edge"
    OPERA = "opera"
    BRAVE = "brave"


class OS(Enum):
    """Supported operating systems."""
    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"
    ANDROID = "android"
    IOS = "ios"


class DeviceType(Enum):
    """Device type categories."""
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"


# Chrome versions (recent stable releases - Dec 2025)
CHROME_VERSIONS = [
    "143.0.7499.40", "143.0.7499.29", "142.0.7444.163", "142.0.7444.142",
    "141.0.7388.120", "141.0.7388.98", "140.0.7331.115", "140.0.7331.94",
    "139.0.7275.89", "139.0.7275.64", "138.0.7220.75", "138.0.7220.52",
    "137.0.7165.88", "136.0.7110.76", "135.0.7055.63"
]

# Firefox versions (Dec 2025)
FIREFOX_VERSIONS = [
    "145.0.2", "145.0.1", "145.0", "144.0.2", "144.0.1", "144.0",
    "143.0.1", "143.0", "142.0.1", "142.0", "141.0.1", "141.0",
    "140.0.1", "140.0", "139.0", "138.0"
]

# Safari versions (Dec 2025)
SAFARI_VERSIONS = [
    "18.6", "18.5", "18.4", "18.3", "18.2", "18.1.1", "18.1", "18.0.1", "18.0",
    "17.6", "17.5", "17.4.1", "17.4", "17.3", "17.2.1", "17.2"
]

# Edge versions (Dec 2025)
EDGE_VERSIONS = [
    "142.0.3595.94", "142.0.3595.80", "141.0.3534.75", "141.0.3534.62",
    "140.0.3472.89", "140.0.3472.66", "139.0.3410.85", "139.0.3410.52",
    "138.0.3351.78", "137.0.3296.68", "136.0.3240.76"
]

# Opera versions (Dec 2025)
OPERA_VERSIONS = [
    "124.0.5705.65", "124.0.5705.42", "123.0.5648.89", "123.0.5648.65",
    "122.0.5592.78", "122.0.5592.54", "121.0.5538.85", "121.0.5538.62",
    "120.0.5484.76", "119.0.5430.65", "118.0.5376.88"
]

# Windows versions
WINDOWS_VERSIONS = [
    ("10.0", "Windows NT 10.0"),  # Windows 10 & 11 both use NT 10.0
]

# macOS versions (Dec 2025 - Sequoia is macOS 15)
MACOS_VERSIONS = [
    "15_2", "15_1_1", "15_1", "15_0_1", "15_0",  # macOS Sequoia
    "14_7_2", "14_7_1", "14_7", "14_6_1", "14_6", "14_5", "14_4_1", "14_4",  # Sonoma
    "13_7", "13_6_9", "13_6_8"  # Ventura (still supported)
]

# Linux distributions
LINUX_DISTROS = [
    "X11; Linux x86_64",
    "X11; Ubuntu; Linux x86_64",
    "X11; Fedora; Linux x86_64",
    "X11; Linux i686",
]

# Android versions (Dec 2025 - Android 15 is latest)
ANDROID_VERSIONS = [
    "15", "14", "13", "12", "11", "10"
]

# Android devices (2024-2025 flagships)
ANDROID_DEVICES = [
    # Samsung Galaxy S series
    "SM-S928B", "SM-S928U", "SM-S926B", "SM-S926U",  # Galaxy S24 Ultra/Plus
    "SM-S921B", "SM-S921U",  # Galaxy S24
    "SM-S918B", "SM-S918U", "SM-S916B", "SM-S911B",  # Galaxy S23 series
    # Google Pixel
    "Pixel 9 Pro XL", "Pixel 9 Pro", "Pixel 9", "Pixel 9a",
    "Pixel 8 Pro", "Pixel 8", "Pixel 8a", "Pixel 7 Pro", "Pixel 7",
    # OnePlus
    "OnePlus 13", "OnePlus 12", "OnePlus 12R", "OnePlus 11",
    # Xiaomi
    "Xiaomi 14 Ultra", "Xiaomi 14 Pro", "Xiaomi 14", "Xiaomi 13 Pro",
    "Redmi Note 13 Pro", "Redmi Note 13",
    # Others
    "ASUS_AI2401", "ROG Phone 8 Pro", "ROG Phone 8"
]

# iOS versions (Dec 2025 - iOS 18 is latest)
IOS_VERSIONS = [
    "18_2", "18_1_1", "18_1", "18_0_1", "18_0",
    "17_7_2", "17_7_1", "17_7", "17_6_1", "17_6", "17_5_1", "17_5"
]

# iOS devices (iPhone 16/15/14 series + iPads)
IOS_DEVICES = [
    ("iPhone", "iPhone17,3"),   # iPhone 16 Pro Max
    ("iPhone", "iPhone17,4"),   # iPhone 16 Pro
    ("iPhone", "iPhone17,1"),   # iPhone 16 Plus
    ("iPhone", "iPhone17,2"),   # iPhone 16
    ("iPhone", "iPhone16,2"),   # iPhone 15 Pro Max
    ("iPhone", "iPhone16,1"),   # iPhone 15 Pro
    ("iPhone", "iPhone15,5"),   # iPhone 15 Plus
    ("iPhone", "iPhone15,4"),   # iPhone 15
    ("iPhone", "iPhone15,3"),   # iPhone 14 Pro Max
    ("iPhone", "iPhone15,2"),   # iPhone 14 Pro
    ("iPad", "iPad16,3"),       # iPad Pro 13" M4
    ("iPad", "iPad16,4"),       # iPad Pro 11" M4
    ("iPad", "iPad14,11"),      # iPad Air 13" M2
    ("iPad", "iPad14,10"),      # iPad Air 11" M2
]

# WebKit versions
WEBKIT_VERSIONS = [
    "537.36", "605.1.15"
]


def _random_string(length: int = 4) -> str:
    """Generate a random alphanumeric string."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def _get_chrome_version() -> str:
    """Get a random Chrome version."""
    return random.choice(CHROME_VERSIONS)


def _get_firefox_version() -> str:
    """Get a random Firefox version."""
    return random.choice(FIREFOX_VERSIONS)


def _get_safari_version() -> str:
    """Get a random Safari version."""
    return random.choice(SAFARI_VERSIONS)


def _get_edge_version() -> str:
    """Get a random Edge version."""
    return random.choice(EDGE_VERSIONS)


def get_chrome_ua(os_type: Optional[OS] = None) -> str:
    """
    Generate a random Chrome User-Agent string.
    
    Args:
        os_type: Optional OS type. If None, randomly selects one.
    
    Returns:
        A realistic Chrome User-Agent string.
    
    Example:
        >>> from pyrua import get_chrome_ua
        >>> ua = get_chrome_ua()
        >>> print(ua)
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...
    """
    if os_type is None:
        os_type = random.choice([OS.WINDOWS, OS.MACOS, OS.LINUX])
    
    chrome_ver = _get_chrome_version()
    
    if os_type == OS.WINDOWS:
        win_ver = random.choice(WINDOWS_VERSIONS)
        platform = f"{win_ver[1]}; Win64; x64"
    elif os_type == OS.MACOS:
        mac_ver = random.choice(MACOS_VERSIONS)
        platform = f"Macintosh; Intel Mac OS X {mac_ver}"
    else:  # Linux
        platform = random.choice(LINUX_DISTROS)
    
    return (
        f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"
    )


def get_firefox_ua(os_type: Optional[OS] = None) -> str:
    """
    Generate a random Firefox User-Agent string.
    
    Args:
        os_type: Optional OS type. If None, randomly selects one.
    
    Returns:
        A realistic Firefox User-Agent string.
    
    Example:
        >>> from pyrua import get_firefox_ua
        >>> ua = get_firefox_ua()
        >>> print(ua)
        Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
    """
    if os_type is None:
        os_type = random.choice([OS.WINDOWS, OS.MACOS, OS.LINUX])
    
    ff_ver = _get_firefox_version()
    
    if os_type == OS.WINDOWS:
        win_ver = random.choice(WINDOWS_VERSIONS)
        platform = f"{win_ver[1]}; Win64; x64"
    elif os_type == OS.MACOS:
        mac_ver = random.choice(MACOS_VERSIONS)
        platform = f"Macintosh; Intel Mac OS X {mac_ver}"
    else:  # Linux
        platform = random.choice(LINUX_DISTROS)
    
    return f"Mozilla/5.0 ({platform}; rv:{ff_ver}) Gecko/20100101 Firefox/{ff_ver}"


def get_safari_ua() -> str:
    """
    Generate a random Safari User-Agent string (macOS/iOS).
    
    Returns:
        A realistic Safari User-Agent string.
    
    Example:
        >>> from pyrua import get_safari_ua
        >>> ua = get_safari_ua()
        >>> print(ua)
        Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 ...
    """
    mac_ver = random.choice(MACOS_VERSIONS)
    safari_ver = _get_safari_version()
    
    return (
        f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_ver}) "
        f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_ver} Safari/605.1.15"
    )


def get_edge_ua(os_type: Optional[OS] = None) -> str:
    """
    Generate a random Microsoft Edge User-Agent string.
    
    Args:
        os_type: Optional OS type. If None, randomly selects one.
    
    Returns:
        A realistic Edge User-Agent string.
    
    Example:
        >>> from pyrua import get_edge_ua
        >>> ua = get_edge_ua()
        >>> print(ua)
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Edg/120.0.2210.91
    """
    if os_type is None:
        os_type = random.choice([OS.WINDOWS, OS.MACOS])
    
    edge_ver = _get_edge_version()
    chrome_ver = _get_chrome_version()
    
    if os_type == OS.WINDOWS:
        win_ver = random.choice(WINDOWS_VERSIONS)
        platform = f"{win_ver[1]}; Win64; x64"
    else:  # macOS
        mac_ver = random.choice(MACOS_VERSIONS)
        platform = f"Macintosh; Intel Mac OS X {mac_ver}"
    
    return (
        f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 Edg/{edge_ver}"
    )


def get_opera_ua(os_type: Optional[OS] = None) -> str:
    """
    Generate a random Opera User-Agent string.
    
    Args:
        os_type: Optional OS type. If None, randomly selects one.
    
    Returns:
        A realistic Opera User-Agent string.
    
    Example:
        >>> from pyrua import get_opera_ua
        >>> ua = get_opera_ua()
        >>> print(ua)
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... OPR/105.0.4970.21
    """
    if os_type is None:
        os_type = random.choice([OS.WINDOWS, OS.MACOS, OS.LINUX])
    
    opera_ver = random.choice(OPERA_VERSIONS)
    chrome_ver = _get_chrome_version()
    
    if os_type == OS.WINDOWS:
        win_ver = random.choice(WINDOWS_VERSIONS)
        platform = f"{win_ver[1]}; Win64; x64"
    elif os_type == OS.MACOS:
        mac_ver = random.choice(MACOS_VERSIONS)
        platform = f"Macintosh; Intel Mac OS X {mac_ver}"
    else:  # Linux
        platform = random.choice(LINUX_DISTROS)
    
    return (
        f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 OPR/{opera_ver}"
    )


def get_android_ua(browser: Optional[Browser] = None) -> str:
    """
    Generate a random Android mobile User-Agent string.
    
    Args:
        browser: Optional browser type. If None, randomly selects Chrome or Firefox.
    
    Returns:
        A realistic Android mobile User-Agent string.
    
    Example:
        >>> from pyrua import get_android_ua
        >>> ua = get_android_ua()
        >>> print(ua)
        Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 ...
    """
    android_ver = random.choice(ANDROID_VERSIONS)
    device = random.choice(ANDROID_DEVICES)
    
    if browser is None:
        browser = random.choice([Browser.CHROME, Browser.FIREFOX])
    
    if browser == Browser.FIREFOX:
        ff_ver = _get_firefox_version()
        return (
            f"Mozilla/5.0 (Android {android_ver}; Mobile; rv:{ff_ver}) "
            f"Gecko/{ff_ver} Firefox/{ff_ver}"
        )
    else:  # Chrome (default for Android)
        chrome_ver = _get_chrome_version()
        return (
            f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 "
            f"(KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
        )


def get_ios_ua(browser: Optional[Browser] = None) -> str:
    """
    Generate a random iOS (iPhone/iPad) User-Agent string.
    
    Args:
        browser: Optional browser type. If None, randomly selects Safari or Chrome.
    
    Returns:
        A realistic iOS User-Agent string.
    
    Example:
        >>> from pyrua import get_ios_ua
        >>> ua = get_ios_ua()
        >>> print(ua)
        Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 ...
    """
    ios_ver = random.choice(IOS_VERSIONS)
    device_name, device_id = random.choice(IOS_DEVICES)
    
    if browser is None:
        browser = random.choice([Browser.SAFARI, Browser.CHROME])
    
    if browser == Browser.CHROME:
        chrome_ver = _get_chrome_version()
        return (
            f"Mozilla/5.0 ({device_name}; CPU {device_name} OS {ios_ver} like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{chrome_ver} Mobile/15E148 Safari/604.1"
        )
    else:  # Safari (default for iOS)
        safari_ver = _get_safari_version()
        return (
            f"Mozilla/5.0 ({device_name}; CPU {device_name} OS {ios_ver} like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_ver} Mobile/15E148 Safari/604.1"
        )


def get_mobile_ua() -> str:
    """
    Generate a random mobile User-Agent string (Android or iOS).
    
    Returns:
        A realistic mobile User-Agent string.
    
    Example:
        >>> from pyrua import get_mobile_ua
        >>> ua = get_mobile_ua()
        >>> print(ua)
    """
    return random.choice([get_android_ua, get_ios_ua])()


def get_desktop_ua(browser: Optional[Browser] = None, os_type: Optional[OS] = None) -> str:
    """
    Generate a random desktop User-Agent string.
    
    Args:
        browser: Optional browser type. If None, randomly selects one.
        os_type: Optional OS type. If None, randomly selects one.
    
    Returns:
        A realistic desktop User-Agent string.
    
    Example:
        >>> from pyrua import get_desktop_ua
        >>> ua = get_desktop_ua()
        >>> print(ua)
    """
    if browser is None:
        # Safari only works on macOS, so exclude it if another OS is specified
        if os_type in (OS.WINDOWS, OS.LINUX):
            browser = random.choice([Browser.CHROME, Browser.FIREFOX, Browser.EDGE, Browser.OPERA])
        else:
            browser = random.choice([Browser.CHROME, Browser.FIREFOX, Browser.SAFARI, Browser.EDGE])
    
    if os_type is None:
        if browser == Browser.SAFARI:
            os_type = OS.MACOS
        else:
            os_type = random.choice([OS.WINDOWS, OS.MACOS, OS.LINUX])
    
    if browser == Browser.CHROME:
        return get_chrome_ua(os_type)
    elif browser == Browser.FIREFOX:
        return get_firefox_ua(os_type)
    elif browser == Browser.SAFARI:
        return get_safari_ua()
    elif browser == Browser.EDGE:
        return get_edge_ua(os_type)
    elif browser == Browser.OPERA:
        return get_opera_ua(os_type)
    else:
        return get_chrome_ua(os_type)


def get_ua(
    browser: Optional[Browser] = None,
    os_type: Optional[OS] = None,
    device_type: Optional[DeviceType] = None
) -> str:
    """
    Generate a customizable random User-Agent string.
    
    Args:
        browser: Optional browser type (Chrome, Firefox, Safari, Edge, Opera).
        os_type: Optional OS type (Windows, macOS, Linux, Android, iOS).
        device_type: Optional device type (desktop, mobile, tablet).
    
    Returns:
        A realistic User-Agent string based on the specified parameters.
    
    Example:
        >>> from pyrua import get_ua, Browser, OS, DeviceType
        >>> ua = get_ua(browser=Browser.CHROME, os_type=OS.WINDOWS)
        >>> print(ua)
        
        >>> ua = get_ua(device_type=DeviceType.MOBILE)
        >>> print(ua)
    """
    # Handle device type priority
    if device_type == DeviceType.MOBILE:
        if os_type == OS.IOS:
            return get_ios_ua(browser)
        elif os_type == OS.ANDROID:
            return get_android_ua(browser)
        else:
            return get_mobile_ua()
    
    if device_type == DeviceType.TABLET:
        # For tablets, use iOS iPad primarily
        return get_ios_ua(browser)
    
    # Handle mobile OS types
    if os_type in (OS.ANDROID, OS.IOS):
        if os_type == OS.ANDROID:
            return get_android_ua(browser)
        else:
            return get_ios_ua(browser)
    
    # Desktop user agents
    return get_desktop_ua(browser, os_type)


def get_rua() -> str:
    """
    Generate a completely random User-Agent string.
    
    This function randomly selects from all available browser/OS combinations
    to generate a realistic User-Agent string.
    
    Returns:
        A random User-Agent string.
    
    Example:
        >>> from pyrua import get_rua
        >>> ua = get_rua()
        >>> print(ua)
    """
    generators = [
        get_chrome_ua,
        get_firefox_ua,
        get_safari_ua,
        get_edge_ua,
        get_opera_ua,
        get_android_ua,
        get_ios_ua,
    ]
    return random.choice(generators)()


def get_rua_list(count: int = 10, unique: bool = True) -> List[str]:
    """
    Generate a list of random User-Agent strings.
    
    Args:
        count: Number of User-Agent strings to generate.
        unique: If True, ensures all User-Agents in the list are unique.
    
    Returns:
        A list of random User-Agent strings.
    
    Example:
        >>> from pyrua import get_rua_list
        >>> ua_list = get_rua_list(5)
        >>> for ua in ua_list:
        ...     print(ua)
    """
    if unique:
        ua_set = set()
        while len(ua_set) < count:
            ua_set.add(get_rua())
        return list(ua_set)
    else:
        return [get_rua() for _ in range(count)]


def get_common_ua() -> str:
    """
    Generate a common, widely-used User-Agent string.
    
    This function generates User-Agents that are statistically more common
    on the web (Chrome on Windows, Safari on macOS, etc.).
    
    Returns:
        A common User-Agent string.
    
    Example:
        >>> from pyrua import get_common_ua
        >>> ua = get_common_ua()
        >>> print(ua)
    """
    # Weighted selection based on browser market share
    browsers = [
        (get_chrome_ua, 65),   # Chrome ~65% market share
        (get_safari_ua, 18),   # Safari ~18% market share
        (get_edge_ua, 5),      # Edge ~5% market share
        (get_firefox_ua, 3),   # Firefox ~3% market share
        (get_android_ua, 7),   # Mobile Chrome/Android
        (get_ios_ua, 2),       # Mobile Safari/iOS
    ]
    
    total = sum(weight for _, weight in browsers)
    r = random.randint(1, total)
    
    cumulative = 0
    for generator, weight in browsers:
        cumulative += weight
        if r <= cumulative:
            return generator()
    
    return get_chrome_ua()  # Fallback


# Legacy support - original Samsung Bada UA
def get_legacy_ua() -> str:
    """
    Generate the original Samsung Bada User-Agent (legacy support).
    
    This is preserved for backward compatibility with the original pyrua module.
    
    Returns:
        A Samsung Bada User-Agent string.
    """
    return (
        f"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/"
        f"{random.randrange(100, 9999)}"
        f"{''.join(random.choices(string.ascii_uppercase, k=4))}"
        f"{random.randrange(1, 9)}; U; Bada/1.2; en-us) "
        f"AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/"
        f"{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B"
    )
