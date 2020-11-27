# -*- coding: utf-8 -*-
# @Time : 2020/10/27 10:03
# @Author : Jiangzhesheng
# @File : depth_tools.py
# @Software: PyCharm
import sys
import myclass
import matplotlib
import matplotlib.pyplot as plt

CHR_ID=0
LOCATION=1
DEPTH=2

class Depthfile(myclass.File_object):

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.id_list=[]
        self.location_list=[]
        self.depth_list=[]

    def __iter__(self):
        depthlines=super().__iter__(1)
        for line in depthlines:
            yield DepthUnit(line)

    def getlist(self):
        if not (self.id_list and self.depth_list and self.location_list):
            self.id_list=[i.chr_id for i in self]
            self.location_list=[i.base_location for i in self]
            self.depth_list=[i.depth for i in self]
        else:
            return

    @property
    def average_depth(self):
        """
        计算平均深度
        :return:
        """
        self.getlist()
        try:
            ans=sum(self.depth_list) / (max(self.location_list) - min(self.location_list) +1)
        except ValueError:
            return 0
        return ans

    @property
    def standard_deviation(self):
        """
        计算depth标准差
        :return:
        """
        avg=self.average_depth
        try:
            location_num=(max(self.location_list) - min(self.location_list) + 1) #碱基个数
            zero_num=(location_num - len(self.depth_list))
            numerator=sum([(i-avg)**2 for i in self.depth_list]) + (avg**2)*zero_num
        except ValueError:
            return 0
        return (numerator/ location_num**2)**0.5
    def plotter(self,title=''):
        self.getlist()
        x_list=self.location_list
        y_list=self.depth_list
        plt.bar(x=x_list,height=y_list,width=1.0)
        plt.xlabel(xlabel='location'),plt.ylabel(ylabel='depth')
        plt.title(label=title if title else self.id_list[CHR_ID])
        plt.show()

class DepthUnit:

    def __init__(self,line='') -> None:
        list=line.split()
        self.chr_id=list[CHR_ID]
        self.base_location=int(list[LOCATION])
        self.depth=int(list[DEPTH])

def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
