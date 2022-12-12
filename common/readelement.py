#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm


class Element(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = f'{name}.yaml'
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError(f"{self.element_path} 文件不存在！")
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        if data := self.data.get(item):
            name, value = data.split('==')
            return name, value
        raise ArithmeticError(f"{self.file_name}中不存在关键字：{item}")


if __name__ == '__main__':
    search = Element('search')
    print(search['搜索框'])
