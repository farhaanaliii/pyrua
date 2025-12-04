"""
Tests for pyrua - Professional Random User-Agent Generator

Run with: pytest tests/ -v
"""

import pytest
from pyrua import (
    get_rua,
    get_ua,
    get_rua_list,
    get_common_ua,
    get_chrome_ua,
    get_firefox_ua,
    get_safari_ua,
    get_edge_ua,
    get_opera_ua,
    get_desktop_ua,
    get_mobile_ua,
    get_android_ua,
    get_ios_ua,
    get_legacy_ua,
    Browser,
    OS,
    DeviceType,
)


class TestBasicFunctions:
    """Test basic User-Agent generation functions."""

    def test_get_rua_returns_string(self):
        """get_rua should return a non-empty string."""
        ua = get_rua()
        assert isinstance(ua, str)
        assert len(ua) > 0

    def test_get_rua_contains_mozilla(self):
        """All modern UAs should contain Mozilla/5.0."""
        ua = get_rua()
        assert "Mozilla/5.0" in ua

    def test_get_rua_randomness(self):
        """Multiple calls should generate different UAs (most of the time)."""
        uas = [get_rua() for _ in range(20)]
        unique_uas = set(uas)
        # At least some should be different
        assert len(unique_uas) > 1

    def test_get_common_ua_returns_string(self):
        """get_common_ua should return a non-empty string."""
        ua = get_common_ua()
        assert isinstance(ua, str)
        assert len(ua) > 0
        assert "Mozilla/5.0" in ua


class TestBrowserSpecificFunctions:
    """Test browser-specific User-Agent generators."""

    def test_get_chrome_ua_format(self):
        """Chrome UA should contain Chrome identifier."""
        ua = get_chrome_ua()
        assert "Chrome/" in ua
        assert "Mozilla/5.0" in ua
        assert "AppleWebKit" in ua

    def test_get_chrome_ua_with_windows(self):
        """Chrome UA with Windows OS."""
        ua = get_chrome_ua(OS.WINDOWS)
        assert "Windows NT" in ua
        assert "Chrome/" in ua

    def test_get_chrome_ua_with_macos(self):
        """Chrome UA with macOS."""
        ua = get_chrome_ua(OS.MACOS)
        assert "Macintosh" in ua
        assert "Mac OS X" in ua
        assert "Chrome/" in ua

    def test_get_chrome_ua_with_linux(self):
        """Chrome UA with Linux."""
        ua = get_chrome_ua(OS.LINUX)
        assert "Linux" in ua
        assert "Chrome/" in ua

    def test_get_firefox_ua_format(self):
        """Firefox UA should contain Firefox identifier."""
        ua = get_firefox_ua()
        assert "Firefox/" in ua
        assert "Mozilla/5.0" in ua
        assert "Gecko" in ua

    def test_get_firefox_ua_with_windows(self):
        """Firefox UA with Windows OS."""
        ua = get_firefox_ua(OS.WINDOWS)
        assert "Windows NT" in ua
        assert "Firefox/" in ua

    def test_get_firefox_ua_with_macos(self):
        """Firefox UA with macOS."""
        ua = get_firefox_ua(OS.MACOS)
        assert "Macintosh" in ua
        assert "Firefox/" in ua

    def test_get_firefox_ua_with_linux(self):
        """Firefox UA with Linux."""
        ua = get_firefox_ua(OS.LINUX)
        assert "Linux" in ua
        assert "Firefox/" in ua

    def test_get_safari_ua_format(self):
        """Safari UA should contain Safari and Version identifiers."""
        ua = get_safari_ua()
        assert "Safari/" in ua
        assert "Version/" in ua
        assert "Macintosh" in ua
        assert "Mac OS X" in ua

    def test_get_edge_ua_format(self):
        """Edge UA should contain Edg identifier."""
        ua = get_edge_ua()
        assert "Edg/" in ua
        assert "Chrome/" in ua  # Edge is Chromium-based
        assert "Mozilla/5.0" in ua

    def test_get_edge_ua_with_windows(self):
        """Edge UA with Windows OS."""
        ua = get_edge_ua(OS.WINDOWS)
        assert "Windows NT" in ua
        assert "Edg/" in ua

    def test_get_edge_ua_with_macos(self):
        """Edge UA with macOS."""
        ua = get_edge_ua(OS.MACOS)
        assert "Macintosh" in ua
        assert "Edg/" in ua

    def test_get_opera_ua_format(self):
        """Opera UA should contain OPR identifier."""
        ua = get_opera_ua()
        assert "OPR/" in ua
        assert "Chrome/" in ua  # Opera is Chromium-based
        assert "Mozilla/5.0" in ua

    def test_get_opera_ua_with_windows(self):
        """Opera UA with Windows OS."""
        ua = get_opera_ua(OS.WINDOWS)
        assert "Windows NT" in ua
        assert "OPR/" in ua

    def test_get_opera_ua_with_linux(self):
        """Opera UA with Linux."""
        ua = get_opera_ua(OS.LINUX)
        assert "Linux" in ua
        assert "OPR/" in ua


class TestDeviceSpecificFunctions:
    """Test device-specific User-Agent generators."""

    def test_get_desktop_ua_returns_string(self):
        """get_desktop_ua should return a valid UA string."""
        ua = get_desktop_ua()
        assert isinstance(ua, str)
        assert "Mozilla/5.0" in ua

    def test_get_desktop_ua_with_browser(self):
        """get_desktop_ua with specific browser."""
        ua = get_desktop_ua(browser=Browser.CHROME)
        assert "Chrome/" in ua

        ua = get_desktop_ua(browser=Browser.FIREFOX)
        assert "Firefox/" in ua

    def test_get_mobile_ua_returns_string(self):
        """get_mobile_ua should return a valid mobile UA string."""
        ua = get_mobile_ua()
        assert isinstance(ua, str)
        assert "Mozilla/5.0" in ua
        # Should contain mobile indicators
        assert "Mobile" in ua or "Android" in ua or "iPhone" in ua or "iPad" in ua

    def test_get_android_ua_format(self):
        """Android UA should contain Android identifier."""
        ua = get_android_ua()
        assert "Android" in ua
        assert "Mozilla/5.0" in ua

    def test_get_android_ua_with_chrome(self):
        """Android UA with Chrome browser."""
        ua = get_android_ua(Browser.CHROME)
        assert "Android" in ua
        assert "Chrome/" in ua
        assert "Mobile" in ua

    def test_get_android_ua_with_firefox(self):
        """Android UA with Firefox browser."""
        ua = get_android_ua(Browser.FIREFOX)
        assert "Android" in ua
        assert "Firefox/" in ua

    def test_get_ios_ua_format(self):
        """iOS UA should contain iPhone or iPad identifier."""
        ua = get_ios_ua()
        assert "Mozilla/5.0" in ua
        assert ("iPhone" in ua or "iPad" in ua)
        assert "like Mac OS X" in ua

    def test_get_ios_ua_with_safari(self):
        """iOS UA with Safari browser."""
        ua = get_ios_ua(Browser.SAFARI)
        assert ("iPhone" in ua or "iPad" in ua)
        assert "Version/" in ua
        assert "Safari/" in ua

    def test_get_ios_ua_with_chrome(self):
        """iOS UA with Chrome browser."""
        ua = get_ios_ua(Browser.CHROME)
        assert ("iPhone" in ua or "iPad" in ua)
        assert "CriOS/" in ua  # Chrome on iOS identifier


class TestCustomizableUA:
    """Test the customizable get_ua function."""

    def test_get_ua_default(self):
        """get_ua with no params should return a valid UA."""
        ua = get_ua()
        assert isinstance(ua, str)
        assert "Mozilla/5.0" in ua

    def test_get_ua_with_browser_chrome(self):
        """get_ua with Chrome browser."""
        ua = get_ua(browser=Browser.CHROME)
        assert "Chrome/" in ua

    def test_get_ua_with_browser_firefox(self):
        """get_ua with Firefox browser."""
        ua = get_ua(browser=Browser.FIREFOX)
        assert "Firefox/" in ua

    def test_get_ua_with_os_windows(self):
        """get_ua with Windows OS."""
        ua = get_ua(os_type=OS.WINDOWS)
        assert "Windows NT" in ua

    def test_get_ua_with_os_macos(self):
        """get_ua with macOS."""
        ua = get_ua(os_type=OS.MACOS)
        assert "Macintosh" in ua or "Mac OS X" in ua

    def test_get_ua_with_os_android(self):
        """get_ua with Android OS should return mobile UA."""
        ua = get_ua(os_type=OS.ANDROID)
        assert "Android" in ua

    def test_get_ua_with_os_ios(self):
        """get_ua with iOS should return mobile UA."""
        ua = get_ua(os_type=OS.IOS)
        assert ("iPhone" in ua or "iPad" in ua)

    def test_get_ua_with_device_mobile(self):
        """get_ua with mobile device type."""
        ua = get_ua(device_type=DeviceType.MOBILE)
        assert "Mobile" in ua or "Android" in ua or "iPhone" in ua

    def test_get_ua_with_device_desktop(self):
        """get_ua with desktop device type."""
        ua = get_ua(device_type=DeviceType.DESKTOP)
        assert "Windows NT" in ua or "Macintosh" in ua or "Linux" in ua

    def test_get_ua_combined_params(self):
        """get_ua with multiple parameters."""
        ua = get_ua(browser=Browser.CHROME, os_type=OS.WINDOWS)
        assert "Chrome/" in ua
        assert "Windows NT" in ua


class TestBulkGeneration:
    """Test bulk User-Agent generation."""

    def test_get_rua_list_default_count(self):
        """get_rua_list should return 10 UAs by default."""
        ua_list = get_rua_list()
        assert isinstance(ua_list, list)
        assert len(ua_list) == 10

    def test_get_rua_list_custom_count(self):
        """get_rua_list should return specified number of UAs."""
        ua_list = get_rua_list(count=5)
        assert len(ua_list) == 5

        ua_list = get_rua_list(count=25)
        assert len(ua_list) == 25

    def test_get_rua_list_unique(self):
        """get_rua_list with unique=True should return unique UAs."""
        ua_list = get_rua_list(count=20, unique=True)
        assert len(ua_list) == 20
        assert len(set(ua_list)) == 20  # All should be unique

    def test_get_rua_list_non_unique(self):
        """get_rua_list with unique=False may have duplicates."""
        ua_list = get_rua_list(count=10, unique=False)
        assert len(ua_list) == 10
        # All should be valid strings
        for ua in ua_list:
            assert isinstance(ua, str)
            assert "Mozilla/5.0" in ua

    def test_get_rua_list_all_valid(self):
        """All UAs in list should be valid."""
        ua_list = get_rua_list(count=50, unique=True)
        for ua in ua_list:
            assert isinstance(ua, str)
            assert len(ua) > 50  # Reasonable minimum length
            assert "Mozilla/5.0" in ua


class TestLegacySupport:
    """Test legacy/backward compatibility functions."""

    def test_get_legacy_ua_format(self):
        """Legacy UA should be Samsung Bada format."""
        ua = get_legacy_ua()
        assert "SAMSUNG" in ua
        assert "Bada" in ua
        assert "Dolfin" in ua
        assert "Mozilla/5.0" in ua


class TestEnums:
    """Test enum values and usage."""

    def test_browser_enum_values(self):
        """Browser enum should have expected values."""
        assert Browser.CHROME.value == "chrome"
        assert Browser.FIREFOX.value == "firefox"
        assert Browser.SAFARI.value == "safari"
        assert Browser.EDGE.value == "edge"
        assert Browser.OPERA.value == "opera"
        assert Browser.BRAVE.value == "brave"

    def test_os_enum_values(self):
        """OS enum should have expected values."""
        assert OS.WINDOWS.value == "windows"
        assert OS.MACOS.value == "macos"
        assert OS.LINUX.value == "linux"
        assert OS.ANDROID.value == "android"
        assert OS.IOS.value == "ios"

    def test_device_type_enum_values(self):
        """DeviceType enum should have expected values."""
        assert DeviceType.DESKTOP.value == "desktop"
        assert DeviceType.MOBILE.value == "mobile"
        assert DeviceType.TABLET.value == "tablet"


class TestVersionFormats:
    """Test that version numbers in UAs are properly formatted."""

    def test_chrome_version_format(self):
        """Chrome version should follow X.X.X.X format."""
        ua = get_chrome_ua()
        # Extract Chrome version
        import re
        match = re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', ua)
        assert match is not None, f"Chrome version not found in: {ua}"
        version = match.group(1)
        parts = version.split('.')
        assert len(parts) == 4
        assert all(part.isdigit() for part in parts)

    def test_firefox_version_format(self):
        """Firefox version should follow X.X or X.X.X format."""
        ua = get_firefox_ua()
        import re
        match = re.search(r'Firefox/(\d+\.\d+(?:\.\d+)?)', ua)
        assert match is not None, f"Firefox version not found in: {ua}"

    def test_safari_version_format(self):
        """Safari version should follow X.X or X.X.X format."""
        ua = get_safari_ua()
        import re
        match = re.search(r'Version/(\d+\.\d+(?:\.\d+)?)', ua)
        assert match is not None, f"Safari version not found in: {ua}"

    def test_edge_version_format(self):
        """Edge version should follow X.X.X.X format."""
        ua = get_edge_ua()
        import re
        match = re.search(r'Edg/(\d+\.\d+\.\d+\.\d+)', ua)
        assert match is not None, f"Edge version not found in: {ua}"


class TestModuleImports:
    """Test module imports and exports."""

    def test_import_all_functions(self):
        """All documented functions should be importable."""
        from pyrua import get_rua
        from pyrua import get_ua
        from pyrua import get_rua_list
        from pyrua import get_common_ua
        from pyrua import get_chrome_ua
        from pyrua import get_firefox_ua
        from pyrua import get_safari_ua
        from pyrua import get_edge_ua
        from pyrua import get_opera_ua
        from pyrua import get_desktop_ua
        from pyrua import get_mobile_ua
        from pyrua import get_android_ua
        from pyrua import get_ios_ua
        from pyrua import get_legacy_ua

    def test_import_enums(self):
        """All enums should be importable."""
        from pyrua import Browser, OS, DeviceType

    def test_module_version(self):
        """Module should have version attribute."""
        import pyrua
        assert hasattr(pyrua, '__version__')
        assert pyrua.__version__ == "1.0.0"

    def test_module_author(self):
        """Module should have author attribute."""
        import pyrua
        assert hasattr(pyrua, '__author__')
        assert pyrua.__author__ == "Farhan Ali"


class TestEdgeCases:
    """Test edge cases and potential issues."""

    def test_large_list_generation(self):
        """Should handle generating large lists of UAs."""
        ua_list = get_rua_list(count=100, unique=True)
        assert len(ua_list) == 100
        assert len(set(ua_list)) == 100

    def test_repeated_calls_stability(self):
        """Repeated calls should not cause errors."""
        for _ in range(100):
            ua = get_rua()
            assert isinstance(ua, str)
            assert len(ua) > 0

    def test_all_generators_work(self):
        """All generator functions should work without errors."""
        generators = [
            get_rua,
            get_common_ua,
            get_chrome_ua,
            get_firefox_ua,
            get_safari_ua,
            get_edge_ua,
            get_opera_ua,
            get_desktop_ua,
            get_mobile_ua,
            get_android_ua,
            get_ios_ua,
            get_legacy_ua,
        ]
        for gen in generators:
            ua = gen()
            assert isinstance(ua, str)
            assert len(ua) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

