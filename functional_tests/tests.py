#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time
"""Functional Test 功能测试 FT"""


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(3)  # (隐式)等待3秒，以便显示页面

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 你打开了首页
        self.browser.get(self.live_server_url)

        #  你注意到在线待办事项应用网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 你要输入了第一个待办事项，你发现在输入框中有'Enter a to-do item'
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 你在文本框中输入了“Buy peacock feathers”
        inputbox.send_keys('Buy peacock feathers')

        # 按回车，被带到了一个新的URL
        # 这个页面的待办事项清单中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was:\n%s" % (
        #         table.text,
        #     )
        # )

        # 页面又显示了第二个文本框
        # 在第二个文本框中输入第二个待办事项“Use peacock feathers to make a fly”
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 再次更新页面，显示两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )

        # 现在另一个人弗朗西斯来访问网站

        ## 使用一个新的浏览器会话
        ## 确保edith的信息不会从cooki中泄露
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗朗西斯访问首页
        # 页面中没有edith的清单信息
        self.browser.get(self.live_server_url)
        page_next = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_next)
        self.assertNotIn('make a fly', page_next)

        # 弗朗西斯输入一个待办事项，新建一个清单
        # 他不像edith一样兴趣盎然
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 弗朗西斯获得了他的唯一URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个页面没有edith的清单
        page_next = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_next)
        self.assertIn('Buy milk', page_next)

        self.fail('Finish the test!')

        # 再次访问这个URL，待办事项还在


# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
