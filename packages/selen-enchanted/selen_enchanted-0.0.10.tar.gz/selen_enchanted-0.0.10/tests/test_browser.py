import unittest
from unittest.mock import patch, MagicMock
from ..core.browser import Browser

class TestBrowser(unittest.TestCase):
    @patch('browser.ChromeDriver')
    @patch('browser.Logger')
    @patch('browser.Sleeper')
    @patch('browser.Tab')
    @patch('browser.Locator')
    @patch('browser.Actions')
    @patch('browser.JavaScripts')
    @patch('browser.Profiler')
    def setUp(self, MockProfiler, MockJavaScripts, MockActions, MockLocator, MockTab, MockSleeper, MockLogger, MockChromeDriver):
        self.mock_driver = MagicMock()
        MockChromeDriver.return_value.driver = self.mock_driver
        self.mock_logger = MagicMock()
        MockChromeDriver.return_value.logger = self.mock_logger

        self.browser = Browser()

    def test_initialization(self):
        self.assertIsNotNone(self.browser.driver)
        self.assertIsNotNone(self.browser.logger)
        self.assertIsNotNone(self.browser.sleeper)
        self.assertIsNotNone(self.browser.tab)
        self.assertIsNotNone(self.browser.locator)
        self.assertIsNotNone(self.browser.actions)
        self.assertIsNotNone(self.browser.js)
        self.assertIsNotNone(self.browser.keys)
        self.assertIsNotNone(self.browser.By)
        self.assertIsNotNone(self.browser.ActionChains)
        self.assertIsNotNone(self.browser.profile)

    @patch('time.sleep', return_value=None)
    def test_wait(self, mock_sleep):
        self.browser.wait(5)
        mock_sleep.assert_called_once_with(5)

if __name__ == '__main__':
    unittest.main()