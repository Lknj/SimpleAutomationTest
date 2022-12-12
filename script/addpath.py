#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import contextlib
import os
import site

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
USER_PTH = os.path.join(site.getsitepackages()[-1], 'requirements.pth')


def main():
    with contextlib.suppress(FileNotFoundError):
        os.remove(USER_PTH)
    with open(USER_PTH, 'w') as f:
        f.write(BASE_DIR)
        print("生成文件成功！")
        print(f"文件位置：{USER_PTH}")
    with open(USER_PTH) as f:
        print("文件内容：", f.read())


if __name__ == '__main__':
    main()