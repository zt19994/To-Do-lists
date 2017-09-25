#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
"""Functional Test 功能测试 FT"""


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # (隐式)等待3秒，以便显示页面

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开首页
        self.browser.get('http://localhost:8000')

        #  注意到在线待办事项应用网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        # 在文本框中输入了“Buy peacock feathers”
        inputbox.send_keys('Buy peacock feathers')

        # 按回车，页面更新了

        # 在待办事项表格中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )


        # 页面又显示了第二个文本框
        # 在第二个文本框中输入第二个待办事项“Use peacock feathers to make a fly”

        self.fail('Finish the test!')

        # 再次更新页面，显示两个待办事项

        # 网站生成唯一的URL，可以记住你的待办事项
        # 而且页面有一些文字说明这个功能

        # 再次访问这个URL，待办事项还在

if __name__ == '__main__':
    unittest.main(warnings='ignore')