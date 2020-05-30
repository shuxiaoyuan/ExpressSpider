#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/13 11:53
# @Description: chrome spider

import os
import time
import logging
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChromeSpider(Chrome):

    def __init__(self):
        options = Options()
        options.add_argument('--no-sandbox')                        # 解决 DevToolsActivePort 文件不存在的报错
        options.add_argument('window-size=1920x3000')               # 指定浏览器分辨率
        options.add_argument('--disable-gpu')                       # 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars')                   # 隐藏滚动条, 应对一些特殊页面
        # options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        options.add_argument('--headless')                          # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # options.add_argument("user-data-dir=" + USER_DIR)            # 使用当前 chrome 的用户目录数据（需要关闭正在运行的 chrome）
        Chrome.__init__(self, executable_path='./chromedriver.exe', options=options)

        self.__path_save_images = './images/'
        self.__scrollTop = 0
        self.__input_express_num = None
        self.__button_search_express = None
        # self.maximize_window()

    def crawl(self, express_num_list):

        # 访问网站
        self.get('https://www.kuaidi100.com/?from=openv')

        # 定位元素并滑动到该位置
        self.__input_express_num = self.find_element_by_id('postid')
        self.__button_search_express = self.find_element_by_id('query')
        header = self.find_element_by_class_name('header')
        input_express_num = self.find_element_by_class_name('search-absolute')
        self.__scrollTop = input_express_num.location['y'] - header.location['y']
        self.execute_script('document.documentElement.scrollTop=' + str(self.__scrollTop))

        # 批量爬取
        for express_num in express_num_list:
            self.__crawl_one_express(express_num)

    def __crawl_one_express(self, express_num):

        # 模拟输入快递单号查询操作
        self.__input_express_num.send_keys(express_num)
        self.__input_express_num.click()
        time.sleep(0.5)
        self.__button_search_express.click()
        time.sleep(1)

        # 屏幕截图保存后裁剪，删除原图
        self.get_screenshot_as_file('tmp.png')
        ele = self.find_element_by_class_name('search-absolute')
        left = ele.location['x']
        top = ele.location['y'] - self.__scrollTop
        right = left + ele.size['width']
        bottom = top + ele.size['height']
        crop_image = Image.open('tmp.png')
        crop_image = crop_image.crop((left, top, right, bottom))
        crop_image.save(self.__path_save_images + express_num + '.png')
        logger.info(self.__path_save_images + express_num + '.png saved.')
        os.remove('tmp.png')


if __name__ == '__main__':
    chrome_spider = ChromeSpider()
    chrome_spider.crawl(['3832748915345'])
    chrome_spider.quit()
