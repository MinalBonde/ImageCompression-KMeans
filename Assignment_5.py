# Kmeans algorithm for Image Compression.
# @author : Minal Bonde
# output: compressed images for k =2,5,10,15,20 in a same directory of a program 

import cv2
import random
import math
import sys
import os
import ast

class kMeansAlgo:
    def __init__(self,sourceimgPath,k):
        self.sourceimgPath = sourceimgPath
        self.k = k
        self.im = cv2.imread(sourceimgPath)
        if(self.im is None):
            print("Image not found")
            return
        self.height = len(self.im)
        self.width = len(self.im[0])
        self.kMeans = [[0 for x in range(3)] for y in range(self.k)] 
        self.cluster = [[0 for x in range(self.width)] for y in range(self.height)] 
        self.addedArray = [[0 for x in range(3)] for y in range(self.k)]
        self.count = [0 for x in range(k)]
        self.pos = -1
    
    def initializeRandomMeans(self):
        for a in range(0,self.k):
            for b in range(0,3):
                self.kMeans[a][b] = random.randint(0,255)
    
    def calculateMeanValue(self):
        for m in range(0,self.k):
            for l in range(0,3):
                if self.count[m] != 0:
                    self.kMeans[m][l] = self.addedArray[m][l]/self.count[m]
                self.addedArray[m][l] = 0
            self.count[m] = 0
    
    def assignColorToPixels(self):
        for i in range(0, self.height)  :
                for j in range(0, self.width):
                    self.im[i][j] = self.kMeans[self.cluster[i][j]]
                
                
    def kMeansCompressionAlgorithm(self):
        dist = 0
        minDist = -1
        for repetitions in range(0,25):
            for i in range(0, self.height)  :
                for j in range(0, self.width):
                     for kPoint in range(0,self.k):
                         dist = math.sqrt(math.pow((self.kMeans[kPoint][0] - self.im[i][j][0]) , 2)  
                                 + math.pow((self.kMeans[kPoint][1] - self.im[i][j][1]) , 2) 
                                 + math.pow((self.kMeans[kPoint][2] - self.im[i][j][2]) , 2)  )
                         if (minDist == -1 or dist < minDist) : 
                             minDist = dist
                             pos = kPoint
                     if pos != -1:
                         self.cluster[i][j] = pos
                         self.addedArray[pos][0] += self.im[i][j][0] 
                         self.addedArray[pos][1] += self.im[i][j][1] 
                         self.addedArray[pos][2] += self.im[i][j][2] 
                         self.count[pos] = self.count[pos] + 1
                     minDist = -1
            self.calculateMeanValue()
            
    def showimageInWindow(self,k,filename):
        currDir = os.getcwd()
        cv2.imwrite(os.path.join(currDir , str(filename)+'_'+str(k)+'_MeansCompressed.jpg'), self.im)
        cv2.waitKey(0)
    
#Program starts here
if __name__=="__main__":
    
    path = os.getcwd()
    clusters = [2,5,10,15,20]
    for k in clusters:
        filename = 'Koala'
        filepath = os.path.join(path, 'Koala.jpg')
        Obj = kMeansAlgo(filepath , int(k))
        Obj.initializeRandomMeans()
        Obj.kMeansCompressionAlgorithm()
        Obj.assignColorToPixels()
        Obj.showimageInWindow(k,filename)
    
    for k in clusters:
        filename = 'Penguins'
        filepath = os.path.join(path, 'Penguins.jpg')
        Obj = kMeansAlgo(filepath , int(k))
        Obj.initializeRandomMeans()
        Obj.kMeansCompressionAlgorithm()
        Obj.assignColorToPixels()
        Obj.showimageInWindow(k,filename)
    
    
    
    
