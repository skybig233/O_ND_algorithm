# -*- coding: utf-8 -*-
# @Time : 2020/9/16 14:49
# @Author : Jiangzhesheng
# @Site : 
# @File : sam.py.py
# @Software: PyCharm
import sys

READ_ID=0
FLAG=1
REF_ID=2
START=3

class Sam:
    def __init__(self, line='') -> None:
        infolist=line.split()
        self.read_id=infolist[READ_ID]
        self.flag=infolist[FLAG]
        self.ref_id=infolist[REF_ID]
        self.start=infolist[START]
        self.barcode=self.read_id.split('#')[-1]
    def __str__(self) -> str:
        self.string=''


def main(argv):
    pass
if __name__ == '__main__':
    test=Sam('V300017823L1C001R030000008#626_142_1055 147     67      9570626 60      100M    =       9570491 -235    ACTGGTATTCCATTTATGTTGTGGGGCAGATTATTATTCCTGTACATTGAATTGAAACTTTAAAGGATTTACAGCTTTTCAAAATAACCTGATACCACAG    FFFFF@FFFFFFGFGFFGCFFFFFFFFFFFDFDGFEFFFFGFFEFFFFFFFF>GFFFFFFGFFFFEFFFFFFFFFFFFFFFFFGGGFF@CFFFFFFFFFF    NM:i:0  MD:Z:100        AS:i:100        XS:i:19')
    print(test.tolist())
    main(sys.argv)