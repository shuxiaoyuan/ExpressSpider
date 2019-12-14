#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/13 12:38
# @Description: 爬虫入口

from gui import SpiderGUI
from read_excel import ExcelReader
from spider_chrome import ChromeSpider


spider_gui = SpiderGUI()
excel_reader = ExcelReader()
chrome_spider = ChromeSpider()


def crawl(event):
    spider_gui.button_crawl.grid_forget()
    chrome_spider.crawl(excel_reader.get_express_num_list(spider_gui.excel_path))
    spider_gui.show_button_crawl()


def close():
    chrome_spider.quit()
    spider_gui.destroy()


spider_gui.button_crawl.bind('<Button-1>', crawl)
spider_gui.protocol('WM_DELETE_WINDOW', close)
spider_gui.mainloop()
