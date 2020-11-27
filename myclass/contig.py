# -*- coding: utf-8 -*-
# @Time : 2020/9/18 9:24
# @Author : Jiangzhesheng
# @File : contig.py
# @Software: PyCharm
import sys
from myclass import Dna_Sequence
class Contig(Dna_Sequence):
    def __init__(self, base_string='', orient='',on_scaffold='',start=0,end=0) -> None:
        super().__init__(base_string,orient)
        self.scaffold_id=on_scaffold
        self.start=start
        self.end=end

def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
