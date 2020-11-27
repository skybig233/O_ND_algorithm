# -*- coding: utf-8 -*-
# @Time : 2020/9/18 9:23
# @Author : Jiangzhesheng
# @File : gap.py
# @Software: PyCharm
import sys
import argparse
from myclass import Contig
class Gap(Contig):
    def __init__(self,on_scaffold='', start=0, end=0) -> None:
        super().__init__(base_string='',
                         orient='',
                         on_scaffold=on_scaffold,
                         start=start,
                         end=end)
    def to_infostring(self):
        stringlist=[str(self.scaffold_id),str(self.start),str(self.end)]
        return '\t'.join(stringlist)+'\n'
def main(argv):
    pass
if __name__ == '__main__':
    main(sys.argv)