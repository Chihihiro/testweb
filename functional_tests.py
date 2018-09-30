from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_strart(self):
        # 伊迪斯要看首页
        self.browser.get(url="http://127.0.0.1:8000")

        # 她注意到了有todo
        self.assertIn("To-Do", self.browser.title)
        # self.fail('Finish the test!')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Buy peacock' for row in rows)
        )
        self.fail('Finsh the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')



# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get("http://127.0.0.1:8000")
#
# assert "Django" in browser.title













