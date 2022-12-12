#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm
from utils.times import running_time


@running_time
def inspect_element():  # sourcery skip: raise-specific-error
    """检查所有的元素是否正确
    只能做一个简单的检查
    """
    for files in os.listdir(cm.ELEMENT_PATH):
        _path = os.path.join(cm.ELEMENT_PATH, files)
        with open(_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        for k in data.values():
            try:
                pattern, value = k.split('==')
            except ValueError as e:
                raise Exception("元素表达式中没有`==`") from e
            if pattern not in cm.LOCATE_MODE:
                raise Exception(f'{_path}中元素【{k}】没有指定类型')
            elif pattern == 'xpath':
                assert '//' in value, f'{_path}中元素【{k}】xpath类型与值不配'
            elif pattern == 'css':
                assert '//' not in value, f'{_path}中元素【{k}]css类型与值不配'
            else:
                assert value, f'{_path}中元素【{k}】类型与值不匹配'
    print("执行完成！")


if __name__ == '__main__':
    inspect_element()
