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

    def test_can_start_a_todo_list(self):

        # checkout the homepage
        self.browser.get('http://localhost:8000')

        # assertEqual, assertTrue, assertFalse
        # check title and header
        self.assertIn("To-Do", self.browser.title)
        header_test = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertIn("To-Do", header_test)

        # enter a to-do item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # type "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")

        # hits enter and it updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(7)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows),
                        "New to-do item did not appear in table"
                        )



        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')