# Module 06: Selenium with Python

## Preparation:

Read the
[Unofficial Selenium Python documentation](http://selenium-python.readthedocs.io/);

## Installation

1. Download the .tar.gz archive from https://pypi.python.org/pypi/selenium and
   extract the `selenium/` directory into the current directory (or anywhere on the
   Python module search path)
2. Download geckodriver from https://github.com/mozilla/geckodriver/releases and
   extract the `geckodriver.exe` under the Windows search path. If Selenium is not
   able to find `geckodriver.exe` automatically then use:

        driver = webdriver.Firefox(executable_path = 'C:\<path to>\geckodriver.exe')

## Selenium WebDriver basics

1. Driver initialization

        from selenium import webdriver
        driver = webdriver.Firefox()

2. Navigation:

        driver.get(“http://google.com”)


3. Locating elements, see
   [Chapter 4. Locating elements](http://selenium-python.readthedocs.io/locating-elements.html)

        driver.find_element_by_id('loginForm')
        driver.find_elements_by_id('tweetMeButton')

4. Actions:

        from selenium.webdriver.common.keys import Keys
        element.send_keys("some text")
        element.send_keys(" and then some more", Keys.RETURN)
        anyElement.click()
        
        # hover element
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(driver).move_to_element(element).perform()

5. Waits, see [Chapter 5. Waits](http://selenium-python.readthedocs.io/waits.html):

    - Implicit Waits

        This means to poll the DOM for a certain amount of time when trying to find an element
        if they are not immediately available. The default setting is 0. Once set, the implicit
        wait is set for the life of the WebDriver object instance.


            from selenium import webdriver

            driver = webdriver.Firefox()
            driver.implicitly_wait(10) # seconds
            driver.get("http://somedomain/url_that_delays_loading")
            myDynamicElement = driver.find_element_by_id("myDynamicElement")


    - Explicit Waits

        An explicit wait is code you define to wait for a certain condition to occur before proceeding
        further in the code. The worst case of this is `time.sleep()`, which sets the condition to an
        exact time period to wait. There are some convenience methods provided that help you write code
        that will wait only as long as required. `WebDriverWait` in combination with `expected_conditions`
        is one way this can be accomplished.

            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            driver = webdriver.Firefox()
            driver.get("http://somedomain/url_that_delays_loading")
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "myDynamicElement"))
                )
            finally:
                driver.quit()

    - How to get Selenium to wait for page load after a click

        See this
        [blog post](http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html).


6. Handling alerts, see
   [Chapter 7.3 Alerts](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.alert)


        simpleAlert = driver.switch_to_alert()
        alertText = simpleAlert.text
        simpleAlert.accept()


7. Ending test session/execution:
    - `driver.close()` – closes the current browser instance; does not destroy the driver object
    - `driver.quit()` – closes the current browser instance and destroys the driver object;
      Once `driver.quit()` is called, the driver object can’t be used (needs to be re-initialized)

8. Common exceptions, see
   [Chapter 7.1 Exceptions](http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions)
    - `NoSuchElementException` – when no element with the given address exists in the DOM
    - `ElementNotVisibleException` – when an element with the given address exists in the DOM, but is, for some reason, hidden

9. Asserts

    **NOTE:** most Selenium bindings, including these for Python don't have handy asserts to verify
    existence of elements, number of element children or particular properties. You will have to
    locate the required elements and use the base `assert <boolean condition>` statement or assert
    methods which come from your unit testing framework of choice. Possibly couple that with iterating
    over the selected element to inspect its children, etc!

10. Taking Screenshots

        driver.save_screenshot('screenshot.png')
        
        import codecs
        codecs.open('my-page.html', "w", "utf-8").write(driver.page_source)

11. Handling iframes

    See http://selenium-python.readthedocs.io/navigating.html#moving-between-windows-and-frames

        driver.switch_to_frame("frameName")
        driver.switch_to_frame("frameName.0.child")
        driver.switch_to_default_content()

    For non-Python examples see http://toolsqa.com/selenium-webdriver/handling-iframes-using-selenium-webdriver/


## Tasks

Crate test scripts, based on `unittest.TestCase` which automate the following scenarios:

* Go to python.org and verify that the latest download versions for Windows are 3.6.0 and 2.7.13
* Go to python.org and
    - initiate a search for the string "tutorial" using the search form
    - verify that the first link in Results points to https://www.python.org/doc/newstyle and
    - it's title text is "New-style Classes"
* Go to python.org and
    - initiate a search for the string "ala-bala-nica" using the search form
    - verify that the results list is empty
