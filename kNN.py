#coding=utf-8

from numpy import *
import operator
from operator import itemgetter

def setDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0.0,0.0],[0.0,0.1]])
    label=["A","A","B","B"]
    print group.shape
    return  group,label


def classify(inX,group,label,n):
    dataSize=group.shape[0]
    sqlDiffMat=tile(inX,(dataSize,1))
    disDiffMat=sqlDiffMat-group
    sqlDisDiffMat=disDiffMat**2
    sqDistant=sqlDisDiffMat.sum(axis=1)
    resultDis=sqDistant**0.5
    sortedDist=resultDis.argsort()
    classCount={}
    for i in range(n):
        voteLabel=label[sortedDist[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    reSortedDis=sorted(classCount.iteritems(),key=itemgetter(1),reverse=True)
    return reSortedDis[0][0];
        
# group,label=setDataSet()
# cl=classify([0,0], group, label, 3)
# print(cl)
