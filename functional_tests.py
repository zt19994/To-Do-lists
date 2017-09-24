#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
"""Functional Test 功能测试 FT"""


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # (隐式)等待3秒，以便显示页面

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        #  在线待办事项应用To-Do
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 输入一个待办事项Buy peacock feathers

        # 按回车，页面更新了

        # 在待办事项表格中显示了“1：Buy peacock feathers”

        # 输入第二个待办事项

        # 再次更新页面，显示两个待办事项

        # 网站生成唯一的URL，可以记住你的待办事项
        # 而且页面有一些文字说明这个功能

        # 再次访问这个URL，待办事项还在

if __name__ == '__main__':
    unittest.main(warnings='ignore')