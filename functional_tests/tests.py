from selenium import webdriver
from django.test import LiveServerTestCase
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_strart(self):
        # 伊迪斯要看首页
        self.browser.get(self.live_server_url)

        # 她注意到了有todo
        self.assertIn("To-Do", self.browser.title)
        # self.fail('Finish the test!')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacock to make fly')
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(4)

        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )
        # inputbox.send_keys('Buy peacock')
        #
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock', [row.text for row in rows])
        # print(rows)
        # self.assertIn('2: Use peacock make fly', [row.text for row in rows])

        # self.assertTrue(
        #     any(row.text == 'Buy peacock' for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        # self.assertIn('1: Buy peacocl feathers', [row.text for row in rows])

        # self.fail('Finsh the test!')

#
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')















