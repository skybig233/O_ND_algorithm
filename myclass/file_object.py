# -*- coding: utf-8 -*-
# @Time : 2020/9/27 9:42
# @Author : Jiangzhesheng
# @File : file_object.py
# @Software: PyCharm
import sys
import os
class File_object:
    """
    在生信的某些文件中，一个信息单元（unit）的信息，由文件多行提供
    例如fastq文件里面的fastq，一个信息单元（fastq），由4行信息构成：id、base、orient、quality
    File_object是这些文件的父类
    属性：path，文件的路径
    方法：iter，迭代器，每次调用返回一个信息单元（unit）
    """
    def __init__(self,path:str) -> None:
        self.path=os.path.abspath(path)
    def __iter__(self,n:int):
        """
        :param n: number of lines to describe a unit
        :return: iterable string containing lines of one unit
        """
        with open(self.path,mode='r') as fastqfile:
            while True:
                s=''
                for i in range(n):
                    s+=fastqfile.readline()
                if not s:
                    break
                yield s

def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
