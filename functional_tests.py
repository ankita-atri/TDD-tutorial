import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_test):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_test, [row.text for row in rows])

    def test_can_start_a_todo_list(self):

        # checkout the homepage
        self.browser.get('http://localhost:8000')

        # check title and header
        self.assertIn("To-Do", self.browser.title)
        header_test = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_test)

        # enter a to-do item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        inputbox.send_keys("1: Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("2: Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        # self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")


        self.fail("Finish the test!")



if __name__ == '__main__':
    unittest.main(warnings='ignore')