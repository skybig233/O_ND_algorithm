# -*- coding: utf-8 -*-
# @Time : 2020/10/10 8:49
# @Author : Jiangzhesheng
# @File : bed_tools.py
# @Software: PyCharm
import sys
import myclass

CHROM=0
CHROM_START=1
CHROM_END=2
# CHROM_INFO=3

class Bedfile(myclass.File_object):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def __iter__(self):
        bed_lines=super().__iter__(1)
        for line in bed_lines:
            yield Bed(line)

class Bed:
    def __init__(self,line='') -> None:
        tmplist=line.split()
        self.chrom_id=tmplist[CHROM]
        self.chrom_start=int(tmplist[CHROM_START])
        self.chrom_end=int(tmplist[CHROM_END])
        # self.info=tmplist[CHROM_INFO]

    def add_distance(self,distance:int):
        self.chrom_start-=distance
        self.chrom_end+=distance
        if self.chrom_start<0:
            self.chrom_start=0
        return self
def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
