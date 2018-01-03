#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
卡片形式展示
"""
from  sdk.card.BaseCard import BaseCard

class TextCard(BaseCard):

    def __init__(self, content):
        '''
        文本卡片显示的content
        :param content:
        '''
        super(TextCard, self).__init__({content})
        self.data['type'] = "txt"
        self.data['content'] = "%s" % content

    def getData(self):

        return self.data
        # return {
        #     "type": "txt",
        #     "content": self.data['content']
        # }

if __name__ == '__main__':
    pass