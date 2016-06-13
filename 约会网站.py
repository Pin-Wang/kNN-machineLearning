#coding=utf-8
import numpy
import operator
import matplotlib
import matplotlib.pyplot as pyt
from numpy.lib.shape_base import tile
from numpy.core.multiarray import *
import kNN
from kNN import classify

def textRead():
    file=open("C:\Users\Administrator\Desktop\datingTestSet2.txt","r")
    rl=file.readlines()
    length=len(rl)
    dataFromFile=zeros((length,3))
    resultClass=zeros((length,1))
    for i in range(length):
        dataFromFile[i,:]=rl[i].split("\t")[:3]
        resultClass[i,:]=rl[i].split("\t")[3]
    return dataFromFile,resultClass

def auto_toOne(matrix):
    result=zeros((matrix.shape[0],matrix.shape[1]))
    rows=matrix.shape[0];
    coloum=matrix.shape[1];
    ran=zeros((1,coloum));
    ran=matrix.max(0)-matrix.min(0)
    
    norMatrix=matrix-tile(matrix.min(0),(rows,1))
    result=norMatrix/tile(ran,(rows,1))
    return result,ran,matrix.min(0)

dataFromFile,resultClass=textRead()
result,ran,mins=auto_toOne(dataFromFile)
len=result.shape[0]
errCount=0
classsCount=(int)(0.1*len)
for i in range(classsCount):
    r=classify(result[i],result[classsCount:len,:],resultClass[classsCount:len,0],3);
    if(r!=resultClass[i,0]):
       errCount+=1.0
print errCount
print "err is %f" % (errCount/classsCount)  


fig=pyt.figure()
ax=fig.add_subplot(111)
ax.scatter(result[:,0],result[:,1]);
#pyt.show()
