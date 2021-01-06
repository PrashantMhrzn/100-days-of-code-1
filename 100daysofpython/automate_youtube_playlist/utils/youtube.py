from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


class Youtube:
    """Youtube context manager
    Returns:
        WebDriver: WebDriver object
    """

    def __init__(self, url, headless=False):
        """Sets the url and timeout limit for the browser

        Args:
            url (str): Public youtube playlist url
            headless (boolean, optional): Run the browser headlessly, Defaults to False
        """
        self.browser = None
        self.url = url
        self.options = Options()
        self.options.headless = headless

    def __enter__(self):
        self.browser = webdriver.Firefox(options=self.options)
        print("Opening Browser.....")
        try:
            self.browser.get(self.url)
        except TimeoutException:
            print("Browser timed out. Maybe increasing the timeout_limit could help")
        except WebDriverException:
            print("Oops an error occured!")
        return self.browser

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Closing Browser...")
        # if exc_type:
        #     print(exc_type.__name__)
        #     print(exc_value)
        self.browser.quit()

        # Return true to supress the exceptions caused above
        # return True
