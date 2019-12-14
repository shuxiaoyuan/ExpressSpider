#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/12 15:27
# @Description: gui

from tkinter.filedialog import *


class SpiderGUI(Tk):

    def __init__(self):
        Tk.__init__(self)

        # 窗口置顶居中显示
        self.wm_attributes('-topmost', True)
        self.__set_align_center(340, 180)

        # 空行
        Label().grid()

        # 标题
        self.title('Express Spider')
        self.__label_title = Label(text='Express Spider 0.1')
        self.__label_title.grid(row=1, column=3)

        # 空行
        Label().grid()

        # excel 路径
        self.__row_excel_path = 3
        self.__label_excel_path = Label(text='Excel文件路径')
        self.__entry_excel_path = Entry()
        self.__button_select_excel_path = Button(text='选择Excel文件', command=self.__select_excel_path)
        Label().grid(row=self.__row_excel_path, column=0)
        self.__label_excel_path.grid(row=self.__row_excel_path, column=1)
        Label().grid(row=self.__row_excel_path, column=2)
        self.__entry_excel_path.grid(row=self.__row_excel_path, column=3)
        Label().grid(row=self.__row_excel_path, column=4)
        self.__button_select_excel_path.grid(row=self.__row_excel_path, column=5)

        # 空行
        Label().grid()

        # 爬取按钮
        self.__row_crawl_button = 5
        self.__button_crawl = Button(text='爬取', command=self.__show_status)
        self.__button_crawl.grid(row=self.__row_crawl_button, column=3)

        # 空行
        Label().grid()

        # label message
        self.__row_label_process = 7
        self.__text_rest_key = StringVar()
        self.__text_rest_value = StringVar()
        self.__label_rest_key = Label(textvariable=self.__text_rest_key, fg='green')
        self.__label_rest_value = Label(textvariable=self.__text_rest_value, fg='green')
        self.__label_rest_key.grid(row=self.__row_label_process, column=1)
        self.__label_rest_value.grid(row=self.__row_label_process, column=3)

    def __set_align_center(self, width, height):
        width = int(width)
        height = int(height)
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.update()

    def __select_excel_path(self):
        path = askopenfilename()
        if path != '':
            self.__entry_excel_path.delete(0, END)
            self.__entry_excel_path.insert(0, path)

    def __show_status(self):
        self.__button_crawl.grid_forget()
        self.__text_rest_key.set('剩余：')
        self.__text_rest_value.set('100')

    def show_button_crawl(self):
        self.__text_rest_key.set('')
        self.__text_rest_value.set('')
        self.__button_crawl.grid(row=self.__row_crawl_button, column=3)

    @property
    def button_crawl(self):
        return self.__button_crawl

    @property
    def excel_path(self):
        return self.__entry_excel_path.get()


if __name__ == '__main__':
    spider_gui = SpiderGUI()
    spider_gui.mainloop()
