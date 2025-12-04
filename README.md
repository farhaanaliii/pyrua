# pyrua

[![GitHub](https://img.shields.io/github/license/farhaanaliii/pyrua)](https://github.com/farhaanaliii/pyrua/blob/main/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/farhaanaliii/pyrua)](https://github.com/farhaanaliii/pyrua/releases)
[![PyPI](https://img.shields.io/pypi/v/pyrua)](https://pypi.org/project/pyrua/)
[![Python](https://img.shields.io/pypi/pyversions/pyrua)](https://pypi.org/project/pyrua/)
[![Downloads](https://img.shields.io/pypi/dm/pyrua)](https://pypi.org/project/pyrua/)

**Professional Random User-Agent Generator for Python**

A comprehensive, lightweight Python module for generating realistic User-Agent strings for web scraping, testing, and browser simulation. Supports all major browsers, operating systems, and device types.

## Features

-  **Multiple Browsers**: Chrome, Firefox, Safari, Edge, Opera, Brave
-  **All Platforms**: Windows, macOS, Linux, Android, iOS
-  **Device Types**: Desktop, Mobile, Tablet
-  **Customizable**: Filter by browser, OS, or device type
-  **Realistic Distribution**: `get_common_ua()` mimics real-world browser market share
-  **Bulk Generation**: Generate lists of unique User-Agents
-  **Zero Dependencies**: Pure Python, no external packages required
-  **Type Hints**: Full typing support for modern IDEs
-  **Python 3.8+**: Supports all modern Python versions

##  Installation

```bash
pip install pyrua
```

## Quick Start

### Basic Usage

```python
from pyrua import get_rua

# Generate a random User-Agent
user_agent = get_rua()
print(user_agent)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.109 Safari/537.36
```

### Browser-Specific User-Agents

```python
from pyrua import get_chrome_ua, get_firefox_ua, get_safari_ua, get_edge_ua, get_opera_ua

# Chrome User-Agent
chrome_ua = get_chrome_ua()

# Firefox User-Agent
firefox_ua = get_firefox_ua()

# Safari User-Agent
safari_ua = get_safari_ua()

# Edge User-Agent
edge_ua = get_edge_ua()

# Opera User-Agent
opera_ua = get_opera_ua()
```

### Device-Specific User-Agents

```python
from pyrua import get_desktop_ua, get_mobile_ua, get_android_ua, get_ios_ua

# Desktop User-Agent (random browser/OS)
desktop_ua = get_desktop_ua()

# Mobile User-Agent (Android or iOS)
mobile_ua = get_mobile_ua()

# Android-specific
android_ua = get_android_ua()

# iOS-specific (iPhone/iPad)
ios_ua = get_ios_ua()
```

### Advanced Customization

```python
from pyrua import get_ua, Browser, OS, DeviceType

# Chrome on Windows
ua = get_ua(browser=Browser.CHROME, os_type=OS.WINDOWS)

# Firefox on macOS
ua = get_ua(browser=Browser.FIREFOX, os_type=OS.MACOS)

# Any mobile User-Agent
ua = get_ua(device_type=DeviceType.MOBILE)

# Safari on iOS
ua = get_ua(browser=Browser.SAFARI, os_type=OS.IOS)

# Chrome on Android
ua = get_ua(browser=Browser.CHROME, os_type=OS.ANDROID)
```

### Bulk Generation

```python
from pyrua import get_rua_list

# Generate 10 unique random User-Agents
ua_list = get_rua_list(count=10, unique=True)

for ua in ua_list:
    print(ua)
```

### Realistic Distribution

```python
from pyrua import get_common_ua

# Generate User-Agent based on real-world browser market share
# (Chrome ~65%, Safari ~18%, Edge ~5%, Firefox ~3%, etc.)
common_ua = get_common_ua()
```

## 🛠️ Use Cases

### Web Scraping with Requests

```python
import requests
from pyrua import get_rua

headers = {
    'User-Agent': get_rua()
}

response = requests.get('https://example.com', headers=headers)
```

### Selenium WebDriver

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyrua import get_chrome_ua

options = Options()
options.add_argument(f'user-agent={get_chrome_ua()}')

driver = webdriver.Chrome(options=options)
```

### aiohttp Async Requests

```python
import aiohttp
from pyrua import get_rua

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': get_rua()}
        async with session.get(url, headers=headers) as response:
            return await response.text()
```

### httpx Client

```python
import httpx
from pyrua import get_rua

client = httpx.Client(headers={'User-Agent': get_rua()})
response = client.get('https://example.com')
```

### Rotating User-Agents

```python
from pyrua import get_rua_list

# Pre-generate a pool of User-Agents
ua_pool = get_rua_list(count=100, unique=True)

# Use in rotation
import itertools
ua_cycle = itertools.cycle(ua_pool)

for url in urls:
    headers = {'User-Agent': next(ua_cycle)}
    # ... make request
```

## API Reference

### Core Functions

| Function | Description |
|----------|-------------|
| `get_rua()` | Random User-Agent from any browser/device |
| `get_ua(browser, os_type, device_type)` | Customizable User-Agent generation |
| `get_rua_list(count, unique)` | Generate multiple User-Agents |
| `get_common_ua()` | User-Agent based on market share distribution |

### Browser-Specific Functions

| Function | Description |
|----------|-------------|
| `get_chrome_ua(os_type)` | Chrome User-Agent |
| `get_firefox_ua(os_type)` | Firefox User-Agent |
| `get_safari_ua()` | Safari User-Agent (macOS) |
| `get_edge_ua(os_type)` | Microsoft Edge User-Agent |
| `get_opera_ua(os_type)` | Opera User-Agent |

### Device-Specific Functions

| Function | Description |
|----------|-------------|
| `get_desktop_ua(browser, os_type)` | Desktop User-Agent |
| `get_mobile_ua()` | Mobile User-Agent (Android/iOS) |
| `get_android_ua(browser)` | Android User-Agent |
| `get_ios_ua(browser)` | iOS User-Agent (iPhone/iPad) |

### Enums

```python
from pyrua import Browser, OS, DeviceType

# Browser options
Browser.CHROME, Browser.FIREFOX, Browser.SAFARI, Browser.EDGE, Browser.OPERA, Browser.BRAVE

# OS options
OS.WINDOWS, OS.MACOS, OS.LINUX, OS.ANDROID, OS.IOS

# Device types
DeviceType.DESKTOP, DeviceType.MOBILE, DeviceType.TABLET
```

## Migration from v0.x

If you're upgrading from the original version, the `get_rua()` function still works but now returns modern browser User-Agents. For the original Samsung Bada User-Agent, use:

```python
from pyrua import get_legacy_ua

legacy_ua = get_legacy_ua()
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/farhaanaliii/pyrua.git
cd pyrua

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black pyrua/
isort pyrua/

# Type checking
mypy pyrua/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for realistic User-Agent strings in web scraping projects
- Browser version data sourced from real-world browser release information

## Contact

- **Author**: Farhan Ali
- **GitHub**: [@farhaanaliii](https://github.com/farhaanaliii)
- **Project Link**: [https://github.com/farhaanaliii/pyrua](https://github.com/farhaanaliii/pyrua)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
