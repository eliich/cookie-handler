# cookie_handler
Simple code to fix `Error: cookies[0].sameSite: expected one of (Strict|Lax|None)` and prepare cookies for use in playwright or selenium

## How to Use

### Playwright
```python
from cookie_handler import read_and_modify_cookies

browser = playwright.firefox.launch(headless=False, firefox_user_prefs={"media.peerconnection.enabled": False}) # set browser/proxy settings

    # Create a new browser context and a new page
    context = browser.new_context()
    page = context.new_page()

    # Read cookies from the text file
    cookies = read_and_modify_cookies('C:/Path/To/Cookies.txt') # cookie_handler code

    # Add cookies to the context
    context.add_cookies(cookies)

    # Navigate to the desired URL
    page.goto('https://www.example.com')
```

### Selenium
Please note that Selenium requires you to navigate to the domain before loading cookies, this is due to the higher level of abstraction Selenium has compared to PlayWright and the constraints of SOP(Same-Origin-Policy).
```python
from cookie_handler import read_and_modify_cookies

def run():
    # Launch Firefox
    driver = Firefox(service=Service(GeckoDriverManager().install()))

    # Navigate to a page to set up cookies
    driver.get('https://www.example.com')

    # Load and set cookies
    cookies = read_cookies_from_file('C:/Path/To/Cookies.txt') # cookie_handler code
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Navigate to the target URL
    driver.get('https://www.example.com/example')
```
