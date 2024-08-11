# Standard Libraries
import random
import time

# Third-party Libraries
from lytils import cinput, print_trace, pause
from lytils.file import LyFile
from lytils.logger import LyLogger
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# * OPTIONAL IMPORTS
try:
    import undetected_chromedriver as uc
except ModuleNotFoundError:
    uc = None

try:
    from seleniumwire import webdriver as sw
except ModuleNotFoundError:
    sw = None

# Local Libraries
# Make it so installing browsermobproxy is optional
from .browsermob_proxy_wrapper import BrowsermobProxyWrapper
from .exceptions import SeleniumWireAndUndetectedChromedriverIncompatible
from .exceptions import SeleniumWireNotInstalled
from .exceptions import UndetectedChromedriverNotInstalled
from .locator import QSeleniumLocator


class QSelenium(QSeleniumLocator):
    def __init__(
        self,
        chrome_options: dict,
        chrome_capabilities: dict = {},
        driver_path: str = "",
        clear_cookies: bool = False,
        bmp_options: dict = {},  # browsermob proxy
        use_selenium_wire: bool = False,
        use_undetected_chromedriver: bool = False,
        initialize_driver: bool = True,
        timeout_default: int = 10,
        use_logger: bool = False,
    ):
        # * Raise errors IMMEDIATELY if desired imports are not available
        if use_selenium_wire and use_undetected_chromedriver:
            raise SeleniumWireAndUndetectedChromedriverIncompatible
        if use_selenium_wire and sw == None:
            # ! If selenium-wire is installed, and we are still raising this exception:
            # ! it could be because the blinker package introduced a breaking change in 1.8.0+
            # * It should work if you use blinker@1.7.0
            raise SeleniumWireNotInstalled
        if use_undetected_chromedriver and uc == None:
            raise UndetectedChromedriverNotInstalled

        self.logger = LyLogger("QSelenium", use_logger=use_logger)

        self._use_sw = use_selenium_wire
        self._use_uc = use_undetected_chromedriver
        self._timeout_default = timeout_default

        # * Set DEFAULT headers here
        self._headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US;en;q=0.9",
            "accept-encoding": "gzip, deflate, br",
        }

        # Use browsermob proxy for scraping network traffic
        self._bmp = None
        if bmp_options:
            self.initialize_bmp(bmp_options)

        # Set chrome options
        self._chrome_options = None
        self._set_chrome_options(chrome_options)

        # Set chrome capabilities
        self._chrome_capabilities = None
        self._set_chrome_capabilities(chrome_capabilities)

        # Set chromedriver path
        self._driver_path = None
        chrome_version = chrome_options.get("version", "")
        self._set_driver_path(driver_path, chrome_version)

        # Automatically initialize the driver by default on object creation.
        self._dr = None
        if initialize_driver:
            self.initialize_driver()

            # Try this to avoid tracking cookies potentially flagging your bot.
            if clear_cookies:
                self._clear_cookies()

            # Set real request headers for more sleuth
            self.set_headers()

        self._actions = None  # Use action chains

        # End of object initialization.

    def close(self):
        """
        Teardown Function
        """
        # Close driver if it was initialized
        if self._dr:
            self._dr.close()
            self._dr.quit()
            self.logger.info("Driver closed.")

        # Close browsermob-proxy if it exists
        if self._bmp:
            self._bmp.close()
            self.logger.info("Browsermob-proxy server closed.")

    # * PRIVATE Functions START
    # region
    def _get_seleniumwire_options(self, proxy_url: str):
        # Return the seleniumwire_options to be used with seleniumwire.webdriver.Chrome
        return {
            "proxy": {
                "http": f"{proxy_url}",
                "https": f"{proxy_url}",
                "verify_ssl": True,
            },
        }

    def _set_driver_path(self, path: str = "", version: str = ""):
        if version != "":
            v = version
            self.logger.info(f"Chrome Version: {v}")

            # Automatically installs chromedriver with specified version
            try:
                self._driver_path = ChromeDriverManager(version=v).install()
            except:
                # Alternative parameter name: driver_version
                self._driver_path = ChromeDriverManager(driver_version=v).install()

        elif path != "":
            self._driver_path = path
        else:
            self._driver_path = None

        self.logger.info(f"Driver Path: {self._driver_path}")

    def _set_chrome_options(self, chrome_options: dict):
        o = ChromeOptions()

        # Adding argument to disable the AutomationControlled flag
        o.add_argument("--disable-blink-features=AutomationControlled")

        # Exclude the collection of enable-automation switches
        o.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Turn-off userAutomationExtension
        o.add_experimental_option("useAutomationExtension", False)

        if self._use_uc:
            o = uc.ChromeOptions()
        else:
            # * Options that don't work in undetected chromedriver
            # Keep browser open after completion so we can debug issues
            if chrome_options.get("detach", False):
                o.add_experimental_option("detach", True)

            # Should remove unnecessary errors and warnings
            o.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Maximize browser
        o.add_argument("--start-maximized")

        # Automatically block notifications
        o.add_argument("--disable-notifications")

        # Don"t want extensions to mess up bot
        o.add_argument("--disable-extensions")
        o.add_argument("--disable-default-apps")
        # o.add_argument('--ignore-certificate-errors')
        # o.add_argument('--ignore-ssl-errors')
        # Adding to fix graphical glitch with chrome
        o.add_argument("--disable-gpu")

        # o.add_argument('--disable-site-isolation-trials')
        # o.add_argument('--no-sandbox')
        # o.add_argument('--disable-dev-shm-usage')
        # o.add_argument("--no-default-browser-check")
        # o.add_argument("--no-first-run")
        # o.binary_location = 'G:\My Drive\Programs\Google Chrome\GoogleChromePortable\App\Chrome-bin\chrome.exe'

        if chrome_options.get("user_data_path"):
            o.add_argument(f'--user-data-dir={chrome_options["user_data_path"]}')
            self.logger.debug(f"User Data Path: {chrome_options['user_data_path']}")
        if chrome_options.get("profile_path"):
            o.add_argument(f'--profile-directory={chrome_options["profile_path"]}')
            self.logger.debug(f"Profile Path: {chrome_options['profile_path']}")
        if chrome_options.get("headless"):
            o.add_argument(f"--headless")

        if chrome_options.get("binary_location"):
            o.binary_location = chrome_options["binary_location"]
            self.logger.debug(f"Chrome Binary Path: {o.binary_location}")

        # Utilizing browsermob proxy
        if self._bmp is not None:
            o.add_argument(f"--proxy-server={self._bmp.proxy_url()}")
            self.logger.debug(f"Proxy Server: {self._bmp.proxy_url()}")

        prefs = {}

        # Block images from loading
        if chrome_options.get("block_images", False):
            prefs["profile.managed_default_content_settings.images"] = 2

        if prefs:
            o.add_experimental_option("prefs", prefs)

        self._chrome_options = o
        return self._chrome_options

    def _set_chrome_capabilities(self, chrome_capabilities: dict):
        c = DesiredCapabilities.CHROME.copy()

        # capabilities["acceptSslCerts"] = True

        # Use when receiving the chrome error: ERR_CERT_AUTHORITY_INVALID
        # capabilities["acceptInsecureCerts"] = True
        # capabilities['pageLoadStrategy'] = "normal", "eager", "none"

        c.update(chrome_capabilities)

        # ? Adjust cache for browser to store more data as cache and for longer
        # capabilities["browser_cache"] = {"enabled": True, "capacity": 10000000, "timeToLiveInSeconds": 300}
        self._chrome_capabilities = c
        return self._chrome_capabilities

    def _remove_navigator_webdriver(self):
        """
        Sets navigator.webdriver to undefined to avoid detection.
        """
        script = "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        self._dr.execute_script(script)

    def _set_driver(self):
        chrome_params = {"options": self._chrome_options}
        if self._use_sw and self._bmp is not None:
            chrome_params.update(
                {
                    "seleniumwire_options": self._get_seleniumwire_options(
                        f"http://{self._bmp.proxy_url()}"
                    ),
                }
            )

        if self._use_uc:
            chrome_params.update(
                {
                    "driver_executable_path": self._driver_path,
                    "browser_executable_path": self._chrome_options.binary_location,
                }
            )
        else:
            chrome_params.update({"service": Service(self._driver_path)})

        if self._use_uc:
            self._dr = uc.Chrome(**chrome_params)
        elif self._use_sw:
            self._dr = sw.Chrome(**chrome_params)
        else:
            self._dr = Chrome(**chrome_params)

        # After setting driver, initialize QSeleniumLocator
        QSeleniumLocator.__init__(self, self._dr, self._timeout_default)

        self._remove_navigator_webdriver()

    def _clear_cookies(self):
        self._dr.delete_all_cookies()

    # endregion
    # * PRIVATE Functions END

    # Some websites may require specific cookies in order to categorize you as a real user.
    # To pull existing cookies, follow instructions on https://github.com/GGLionCross/CookieConverter
    # This must be called on the correct domain, or you'll get an InvalidCookieDomainException
    def add_cookies(self, cookies: list[dict]):
        """
        Some websites may require specific cookies in order to categorize you as a real user.
        To pull existing cookies, follow instructions on https://github.com/GGLionCross/CookieConverter
        This must be called on the correct domain, or you'll get an InvalidCookieDomainException
        """
        for cookie in cookies:
            self._dr.add_cookie(cookie)

    def initialize_driver(self):
        try:
            self._set_driver()
        except WebDriverException:
            warning = "Google profile may be in use. If so, please close and press <enter> to continue."
            print_trace()
            cinput(f"<y>{warning}")
            self._set_driver()
        except Exception:
            print_trace()

        return self._dr

    def get_driver(self):
        return self._dr

    def set_headers(self, headers: dict = {}):
        self._headers.update(headers)

        def interceptor(request):
            # Delete previous headers to prevent duplicates
            # Then set real request headers
            for key, value in list(self._headers.items()):
                del self._headers[key]
                self._headers[key] = value

        # Set the Selenium Wire interceptor
        self._dr.request_interceptor = interceptor

    def get_headers(self):
        return self._headers

    # * BROWSERMOB PROXY Functions START
    # region
    """
    Useful for scraping network traffic instead of web elements
    Using network traffic to scrape is often better b/c network traffic is
    less likely to change versus front-end design
    """

    def initialize_bmp(self, bmp_options: dict = {}):
        self._bmp = BrowsermobProxyWrapper(**bmp_options)
        self._bmp.start_server()
        self._bmp.start_client()
        return self._bmp

    def get_bmp(self):
        return self._bmp

    # endregion
    # * BROWSERMOB PROXY Functions END

    # * DEBUG Functions START
    # region
    def pause(self):
        pause()

    def screenshot(self, filepath: str = "images/screenshot.png"):
        file = LyFile(filepath)
        if not file.exists():
            file.create()
        self._dr.save_screenshot(filepath)

    # endregion
    # * DEBUG Functions END

    def use_actions(self):
        self._actions = ActionChains(self._dr)
        return self._actions

    # * DELAY Functions START
    # region
    def random_delay(self, min_delay: int, max_delay: int):
        time.sleep(random.uniform(min_delay, max_delay))

    # Delay functions will be useful so we're not traversing sites at unrealistic speeds
    def visit_with_delay(self, url: str, min_delay: int = 1, max_delay: int = 3):
        # Add delay when visiting url
        self.random_delay(min_delay, max_delay)
        self._dr.get(url)

    def exponential_backoff(self, url: str, max_retries: int = 3, wait_time: int = 1):
        """
        Useful when dealing with multiple requests to a site's server
        @param max_retries: Maximum number of retries to load a page
        @param wait_time: Initial wait time (in seconds) which gets doubled after each failure
        """
        time.sleep(wait_time)
        for i in range(max_retries):
            try:
                self._dr.get(url)
                break  # Break out of for loop if url is successful
            except TimeoutException as e:
                print(f"Failed getting url ({i + 1}): {e}")

                # If error occurs, wait_time is exponentially increased
                wait_time *= 2
                time.sleep(wait_time)

    # endregion
    # * DELAY Functions END
