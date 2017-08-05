from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    # method override
    def __init__(self, driver):
        # call parent class method
        super(MainPage, self).__init__(driver)
        # navigate to the correct URL
        self.driver.get('http://python.org')

    def search_for(self, find_me):
        search_field = self.driver.find_element_by_id('id-search-field')
        search_field.send_keys(find_me, Keys.RETURN)


class SearchResults(BasePage):
    # helper variable to optimize HTML elements search
    _results = None

    # variant 1 with optimization
    # def results(self):
    #     if self._results is None:
    #         self._results = []
    #
    #         main_content = self.driver.find_element_by_class_name('main-content')
    #         ul = main_content.find_element_by_css_selector('form > ul')
    #         assert ul != None
    #         for a in ul.find_elements_by_tag_name('a'):
    #             self._results.append(a)
    #
    #     return self._results


    # variant 2 w/o optimization
    def results(self):
        R = []

        main_content = self.driver.find_element_by_class_name('main-content')
        ul = main_content.find_element_by_css_selector('form > ul')
        assert ul != None
        for a in ul.find_elements_by_tag_name('a'):
            print a.text
            R.append(a)

        return R

